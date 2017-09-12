# -*- coding: utf-8 -*-
'''
Program: DellScrapping/Output Files
Dev: Fabricio Roberto Reinert
Date: 11/09/2017
'''

def save_json_from_dell(path, extension, assets_list) -> bool:
    '''Retrieve a JSON file containing all equipments'''
    try:
        assets_list = MultipleQueryOEM(assets_list)
        JSON = assets_list.json_from_dell()
        fopen = open(path + '.' + extension, 'w')
        fopen.write(JSON)
        fopen.close()
    except:
        return False
    finally:
        return True