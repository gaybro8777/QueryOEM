# -*- coding: utf-8 -*-
"""
Program: DellScrapping/Settings
Dev: Fabricio Roberto Reinert
Date: 30/06/2017

Conf is a submodule to deal with settings at user level
user will be able to specify a dictionary 
or the module will load default values 
"""

from . import default_settings
from ..errors import SettingsConsistency

class Settings:
    '''Retrieve a dict of settings'''

    def __init__(self, **settings):

        self.settings = {}

        if not 'DELL_SUPORT_URL' in settings:
            self.settings['HOME_URL'] = default_settings.DELL_SUPORT_URL
        
        if not 'DELL_SERIAL_INPUT_ID' in settings:
            self.settings['SERIAL_INPUT_ID'] = default_settings.DELL_SERIAL_INPUT_ID

    def conf(self):
        return self.settings