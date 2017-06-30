# -*- coding: utf-8 -*-
'''
Program: DellScrapping/TestUnit
Dev: Fabricio Roberto Reinert
Date: 30/06/2017
'''

if __package__:
    from . import scrapping
else:
    import scrapping

part_nums = ['65G7CD2']
try:
    obj = scrapping.Dell(part_nums)
except:
    print("Error instantiating main Class")