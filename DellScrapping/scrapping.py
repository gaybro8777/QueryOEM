'''
Program: DellScrapping/Main
Dev: Fabricio Roberto Reinert
Date: 30/06/2017

Core of this module.

Make sure you understand the the Requests lib & Beatifull Soup 4 lib
before reading this code. It'll change your life, i promisse you!
'''

import requests

try:
    if __name__ == "__main__":
        import settings, errors    
    else:
        from . import errors, settings

except ImportError as e:
    raise

# Check Settings Consistency
if not settings.DELL_SUPORT_URL:
    raise errors.SettingsConsistency("DELL_SUPPORT_URL")

if not settings.DELL_SERIAL_INPUT_ID:
    raise errors.SettingsConsistency("DELL_SERIAL_INPUT_ID")

class Dell:
    '''Dell Connectivity'''

    def __init__(self, *serial_numbers):
        
        if serial_numbers.len() == 0:
            raise InvalidSerialList("At least one serial need to be passed")

        self.serial_list = serial_numbers