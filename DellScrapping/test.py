# -*- coding: utf-8 -*-
'''
Program: DellScrapping/TestUnit
Dev: Fabricio Roberto Reinert
Date: 30/06/2017
'''

import scrapping
import conf

part_nums = ['65G7CD2']

try:
    obj = scrapping.ScrappingOEM(part_nums)
except BaseException as e:
    print(">> Error instantiating main Class: {0}".format(e))
    raise