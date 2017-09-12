# -*- coding: utf-8 -*-
'''
Program: Scrapping/Output CLI
Dev: Fabricio Roberto Reinert
Date: 11/09/2017
'''
from sys import argv

cli_help ='''
---------------------------
QueryOEM CLI - Single Tag
---------------------------
Arguments
    - (Required) vendor - OEM to Query (Only Dell available)
    - (Required) tag - Service tag of the device 
Example:
    - python -m QueryOEM dell XXXXXXX
'''

def dell_single_asset(tag):
    query = QueryOEM.QueryOEM(PART_NUMBER=tag)
    query.get_from_dell()
    return my_laptop.dell_data

def query_oem(*args):
    '''Query a single tag. Designed to use with "python -m QueryOEM"'''
    leng = len(args)
    arguments = {}

    if leng != 3:
        print('>> There are required parameters missing')
        print(cli_help)
        return

    arguments['vendor'] = args[1]
    arguments['tag'] = args[2]

    # Query Dell
    if upper(arguments['vendor']) == 'DELL':
        return dell_single_asset(upper(arguments['tag']))
    else:
        print('>> Invalid arguments')
        print(cli_help)
        return

if __name__ == '__main__':
    print('>> Requesting data from OEM...')
    result = query_oem(*argv)
    print(result)
