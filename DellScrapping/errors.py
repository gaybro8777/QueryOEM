'''
Program: DellScrapping/Exceptions
Dev: Fabricio Roberto Reinert
Date: 30/06/2017
'''

class SettingsConsistency(Exception):
    '''Used to raise exceptions regarding the module Settings'''

    def __init__(self, field):
        super(SettingsConsistency, self).__init__(self, "Variable {0} is not properly configured".format(field))

class InvalidSerialList(self, arg):
    '''Used to raise exceptions regarding the Serial List '''
    
    def __init__(self, text):
        super(SettingsConsistency, self).__init__(self, "Serial List error: ".format(text))