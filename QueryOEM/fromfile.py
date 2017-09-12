# -*- coding: utf-8 -*-
'''
Program: DellScrapping/Standalone
Dev: Fabricio Roberto Reinert
Date: 11/09/2017
'''
from os import path
from pathlib import Path
from QueryOEM.scrapping import check_format, check_oem
import QueryOEM.outputfile as outputFile

cli_help ='''
---------------------------
Application Trial Extender
---------------------------
Arguments
    - (Required) origin - Path to file containing service tags (1 per line)
    - (Required) output - Path to output file: Path to save output file
    - (Optional) vendor - Vendor - Default Dell
    - (Optional) format - Output format - Default JSON 
Example:
    - python -m QueryOEM.fromfile origin=path/to/mytags.txt output=temp/file vendor=dell format=json
    - python -m QueryOEM.fromfile origin=path/mytags.txt output=file format=json
    - python -m QueryOEM.fromfile origin=path/mytags.txt output=c:/temp/result vendor=dell
    - python -m QueryOEM.fromfile origin=path/mytags.txt output=result format=json
'''

def service_tag_from_file(origin):
    '''reads the file containing tags and return a list of it'''
    fopen = open(origin, 'r')
    return fopen.readlines()

def run(*args):
    '''Run the module with "python -m"'''
    
    arguments = {}
    leng = len(args)

    # Check if required args are passed
    if  3 < leng > 5:
        print('>> There are required parameters missing')
        print(cli_help)
        return

    elif len(args) > 2:
        for arg in args[1:]:
            try:
                split_arg = arg.split('=')
                arguments[split_arg[0]] = split_arg[1]
            except:
                print('>>Malformed parameters')
                print(cli_help)
                return
    
    # Check if we got the required params
    if 'origin' not in arguments.keys():
        print('>> Parameter ORIGIN not informed')
        print(cli_help)
        return

    if 'output' not in arguments.keys():
        print('>> Parameter OUTPUT not informed')
        print(cli_help)
        return

    if 'vendor' not in arguments.keys():
        arguments['vendor'] = 'DELL'

    if 'format' not in arguments.keys():
        arguments['format'] = 'JSON'

    # Check if tag file is valid
    if not arguments['origin'].is_file():
        print('>> File containing tags is invalid')
        print(cli_help)
        return

    # Check if target folder is valid
    if not arguments['output'].is_dir():
        print('>> Output path is invalid')
        print(cli_help)
        return

    # check if OEM typed is available
    if not check_oem(arguments['vendor']):
        print('>> This vendor is not available')
        print(cli_help)
        return

    # check if format is valid
    if not check_format(arguments['format']):
        print('>> File format not supported')
        print(cli_help)
        return

    # Get Tags from file
    tag_list = service_tag_from_file(arguments['origin'])
    
    # Save JSON file from Dell
    if upper(arguments['format']) == 'JSON' and upper(arguments['vendor'] == 'DELL'): 
        outputFile.save_json_from_dell(arguments['output'], arguments['format'], tag_list)

if __name__ == '__main__':
    run(*argv)