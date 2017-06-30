# -*- coding: utf-8 -*-
'''
Program: DellScrapping/Main
Dev: Fabricio Roberto Reinert
Date: 30/06/2017

Core of this module.
Make sure you understand the the Requests lib & Beatifull Soup 4 lib
before reading this code. It'll change your life, i promisse you!
'''

import requests
from bs4 import BeautifulSoup

class ScrappingOEM:
    '''Class responsible for the Scrapping'''

    def __init__(self, *serial_numbers, **settings):

        if len(serial_numbers) == 0:
            raise errors.InvalidSerialList("At least one serial need to be passed")
            
        self.serial_list = serial_numbers

    def run(self):
        '''Worker responsible to run the web scrapping'''
    
        def request_url(self):
            '''Completes the URL request'''
            home = requests.get(settings.DELL_SUPORT_URL)
            
            if home.status_code == 500:
                raise errors.Request500

            elif home.status_code == 404:
                raise errors.Request404

            elif home.status_code != 200:
                raise errors.RequestFailed(home.status_code)

            return home
        
        def html_parser(self, html):
            pass