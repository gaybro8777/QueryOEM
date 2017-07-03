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
import dell
import errors

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
        dell_scrapper = dell.DellScrapper(
            warranty_url=self.settings['DELL_SUPPORT_WARRANTY'],
            config_url=self.settings['DELL_SUPPORT_CONFIG'],
            partnumber=self.settings['PART_NUMBER']
        )
        self.dell_data = dell_scrapper.data




