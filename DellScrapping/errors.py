# -*- coding: utf-8 -*-
'''
Program: DellScrapping/Exceptions
Dev: Fabricio Roberto Reinert
Date: 30/06/2017
'''

class SettingsConsistency(Exception):
    '''Used to raise exceptions regarding the module Settings'''

    def __init__(self, field):
        super(SettingsConsistency, self).__init__(self, "Variable {0} is not properly configured".format(field))

class InvalidSerialList(Exception):
    '''Used to raise exceptions regarding the Serial List '''
    
    def __init__(self, text):
        super(InvalidSerialList, self).__init__(self, "Serial List error: {0}".format(text))

class Request500(Exception):
    '''Raises a 505 - Internal server Error'''

    def __init__(self):
        super(Request500, self).__init__(self, "Host returned 500. Internal Server Error")

class Request404(Exception):
    '''Raises a 404 - Page not found'''

    def __init__(self):
        super(Request500, self).__init__(self, "Host returned 404. Page not found")

class RequestFailed(Exception):
    '''
    Other error codes then 404 or 500 
    could be treaten in here or in a specific Exception
    '''

    def __init__(self, error_code):
        super(RequestFailed, self).__init__(self,str(error_code))

class CheckSettings:
    try:
        if not __package__:
            import settings
            import errors
        else:
            from . import errors, settings
    except ImportError:
        raise

    # Check Settings Consistency
    if not hasattr(settings, 'DELL_SUPORT_URL'):
        raise errors.SettingsConsistency("DELL_SUPPORT_URL")

    if not hasattr(settings, 'DELL_SERIAL_INPUT_ID'):
        raise errors.SettingsConsistency("DELL_SERIAL_INPUT_ID")