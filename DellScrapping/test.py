# -*- coding: utf-8 -*-
'''
Program: DellScrapping/TestUnit
Dev: Fabricio Roberto Reinert
Date: 30/06/2017
'''

import scrapping

# Random service tag to check functionality
part_num = '65G7CD2'

# Instantiate a Scrapper object
try:
    obj = scrapping.ScrappingOEM(PART_NUMBER=part_num)
    obj.get_from_dell()
except BaseException as e:
    print(">> Error instantiating main Class: {0}".format(e))
    raise

print(obj.dell_data)
