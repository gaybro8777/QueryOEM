# -*- coding: utf-8 -*-
"""
Program: DellScrapping/Settings
Dev: Fabricio Roberto Reinert
Date: 30/06/2017

Conf is a submodule to deal with settings at user level
user will be able to specify a dictionary 
or the module will load default values 
"""

# Support URL 
DELL_SUPPORT_URL = "http://www.dell.com/support/home/br/pt/brbsdt1/TagEntry/ValidateSerialNumberEntry"

# ID of the Input which will receive the Serialnumber
DELL_TAGS_INPUT_ID = "inputServiceTag"

class Settings:
    '''Retrieve a dict of settings'''

    def __init__(self, **settings):

        self.settings = {}

        if not 'DELL_SUPPORT_URL' in settings:
            global DELL_SUPPORT_URL
            self.settings['DELL_SUPPORT_URL'] = DELL_SUPPORT_URL
        else:
             self.settings['DELL_SUPPORT_URL'] = settings['DELL_SUPPORT_URL']
        
        if not 'DELL_TAGS_INPUT_ID' in settings:
            global DELL_TAGS_INPUT_ID
            self.settings['DELL_TAGS_INPUT_ID'] = DELL_TAGS_INPUT_ID
        else:
            self.settings['DELL_TAGS_INPUT_ID'] = settings['DELL_TAGS_INPUT_ID']

    def conf(self):
        return self.settings