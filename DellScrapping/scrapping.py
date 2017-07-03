# -*- coding: utf-8 -*-
'''
Program: DellScrapping/Main
Dev: Fabricio Roberto Reinert
Date: 30/06/2017

Core of this module.
Make sure you understand the the Requests lib & Beatifull Soup 4 lib
before reading this code. It'll change your life, i promisse you!

The class DellScrapper need to be up-to-date with Dell's website structure
If you're planning to update it by yourself, do it on the following methods:
    DellScrapper.warranty_to_dict()
    DellScrapper.sysconfig_to_dict()

Don't forget to <return> the result dictionary at the end of the methods!  
'''

import conf
import requests
import errors
import converters
from datetime import datetime
from bs4 import BeautifulSoup as bs

class DellScrapper():
    '''Dell Web scrapping'''

    def __init__(self, **settings):

        # Check information
        if not settings['warranty_url']:
            raise errors.DellScrapperFailure("Failure gathering warranty HTML content")

        if not settings['config_url']:
            raise errors.DellScrapperFailure("Failure gathering system HTML content")

        if not settings['partnumber']:
            raise errors.DellScrapperFailure("Part number not defined")

        # add configuration
        self.conf = settings
        
        # response from DELL's request 
        r_warranty, r_syconfig = self.make_requests(
            warranty_url=self.conf['warranty_url'], 
            sysconfig_url=self.conf['config_url']
        ) 

        # Parse, process and persist data into a dictionary 
        self.data = {
            'warranty': self.warranty_to_dict(r_warranty),
            'sysconfig': self.sysconfig_to_dict(r_syconfig)
        }

    def warranty_to_dict(self, content):
        '''Create a dictionary containing warranty data'''

        b = bs(content, 'html.parser')

        try:
            tr = b.find_all('tr')
            
            # When Dell sended the workstation
            date_send = tr[0].find_all('th')[1].text # Return raw text
            date_send = date_send.replace('Data de envio: ','').replace(',','').replace(' ','') # remove bad chars
            date_send = converters.verb_month_to_number_br(date_send) # Convert to enumerated month
            date_send = datetime.strptime(date_send, '%m%d%Y').strftime('%m/%d/%y') # format date

            # Warranty start date
            start_warranty = tr[2].find_all('td')[1].text # Return raw text
            start_warranty = start_warranty.replace('\r\n', '').replace(',','').replace(' ','') # Remove bad chars
            start_warranty = converters.verb_month_to_number_br(start_warranty) # Convert to enumerated month
            start_warranty = datetime.strptime(start_warranty, '%m%d%Y').strftime('%m/%d/%y') # format date
            
            # Warranty end date
            end_warranty = tr[2].find_all('td')[2].text
            end_warranty = converters.verb_month_to_number_br(end_warranty)
            end_warranty = end_warranty.replace(',','').replace(' ','')
            end_warranty = datetime.strptime(end_warranty, '%m%d%Y').strftime('%m/%d/%y')
        except:
            raise errors.DellScrapperFailure("failed when passing warranty to dict")

        return {
            'sended': date_send,
            'start_warranty': start_warranty,
            'end_warranty': end_warranty,
        }

    def sysconfig_to_dict(self, content):
        '''Create a dictionary containing system configuration'''
        return {'sysconfig_data': ''}

    def make_requests(self, warranty_url, sysconfig_url):
        '''Request data from DELL'''

        def request_warranty(url):
            '''GET request to warranty page'''
            r = requests.get(url.format(self.conf['partnumber']))
            if r.status_code != 200:
                raise errors.RequestFailed(r.status_code)
            return r.content

        def request_system_config(url):
            '''GET request to warranty page'''
            r = requests.get(url.format(self.conf['partnumber']))
            if r.status_code != 200:
                raise errors.RequestFailed(r.status_code)
            return r.content

        response_warranty = request_warranty(warranty_url)
        response_sysconfig = request_system_config(sysconfig_url)

        return response_warranty, response_sysconfig

class ScrappingOEM:
    '''Class responsible for the Scrapping'''

    def __init__(self, **settings):

        # Settings    
        config = conf.Settings(settings=settings)
        self.settings = config.config()

        # Check if partnumber was entered
        if not 'PART_NUMBER' in self.settings:
            raise errors.InvalidSerialList("Part number not informed")

    ### Properties ###
    @property
    def part_number(self):
        '''Will be used to check PN consistency in the future'''
        return self._part_number 

    @property
    def dell_data(self):
        '''Return a dictionary with the scrapped data'''
        return self._dell_data

    ### Setters ###
    @part_number.setter
    def part_number(self, value):
        '''Part Number SETTER''' 
        self._part_number = value

    @dell_data.setter
    def dell_data(self, value):
        self._dell_data = value
        
    ### Methods ###
    def get_from_dell(self):
        '''Issue data from Dell'''
        dell_scrapper = DellScrapper(
            warranty_url=self.settings['DELL_SUPPORT_WARRANTY'],
            config_url=self.settings['DELL_SUPPORT_CONFIG'],
            partnumber=self.settings['PART_NUMBER']
        )
        self.dell_data = dell_scrapper.data




