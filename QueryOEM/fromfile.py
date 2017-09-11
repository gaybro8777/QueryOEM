# -*- coding: utf-8 -*-
'''
Program: DellScrapping/Standalone
Dev: Fabricio Roberto Reinert
Date: 11/09/2017
'''

import QueryOEM
from os import path
from pathlib import Path

cli_help ='''
---------------------------
Application Trial Extender
---------------------------
Arguments
    - Input file: Path to file containing service tags (1 per line)
    - Output folder: Path to save output file
Example:
    - python -m QueryOEM.fromfile mytags.txt c:/temp
'''

def service_tag_from_file(origin):
  '''reads the file containing tags and return a list of it''' 
  fopen = open(origin, 'r')
  return fopen.readlines()

def query_oem(assets, vendor)
  '''Query vendor for data'''
  assets_list = MultipleQueryOEM(assets)
  
  if vendor == 'DELL':
    return assets_list.get_from_dell()
  else:
    return

def save_json(path, assets_list):
  '''Retrieve a JSON containing all equipments'''
  JSON = assets_list.json_from_dell()
  fopen = open(path.join(path,'assets_list.json', 'w')
  fopen.write(JSON)
  fopen.close()

def run(*args):
  '''Run the module with "python -m"'''
  if len(args) != 3:
    print(cli_help)
    return
  
  input_file = Path(args[1])
  output_folder = Path(args[2])

  if !input_file.is_file():
    print('Input file do not exist')
    return

  if !output_folder.is_dir():
    print('Output folder is invalid')
    return 

if __name__ == '__main__':
  run(*argv)