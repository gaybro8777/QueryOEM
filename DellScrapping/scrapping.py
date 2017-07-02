# -*- coding: utf-8 -*-
'''
Program: DellScrapping/Main
Dev: Fabricio Roberto Reinert
Date: 30/06/2017

Core of this module.
Make sure you understand the the Requests lib & Beatifull Soup 4 lib
before reading this code. It'll change your life, i promisse you!
'''

import conf
import requests
import errors
from bs4 import BeautifulSoup

class ScrappingOEM:
    '''Class responsible for the Scrapping'''

    def __init__(self, *serial_numbers, **settings):

        if len(serial_numbers[0]) == 0:
            raise errors.InvalidSerialList("At least one serial need to be passed")

        # Settings    
        config = conf.Settings(settings=settings)
        self.settings = config.conf()
        
        # List of Service Tags
        self.serial_list = serial_numbers

        # Run Web Scrapper
        self.run()

    def run(self):
        '''Worker responsible to run the web scrapping'''
    
        def request_url():
            '''Completes the URL request'''
            for tag in self.serial_list[0]:
                data = {
                    self.settings['DELL_TAGS_INPUT_ID']: tag,
                    'hidSubmitValue': True,
                    'intent': '',
                    'appName': 'mse'
                }
                print(data)
                r = requests.post(self.settings['DELL_SUPPORT_URL'], data=data)
                if r.status_code != 200:
                    raise errors.RequestFailed(r.status_code)
                
            return r

        resp = request_url()
        print(resp.content)

