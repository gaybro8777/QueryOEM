# -*- coding: utf-8 -*-
'''
Program: DellScrapping/TestUnit
Dev: Fabricio Roberto Reinert
Date: 30/06/2017
'''

import scrapping

# Random service tag to check functionality
part_num = '65G7CD2'


def stdout(obj):
    '''Streams out the result'''
    print('Warranty Information:', obj.dell_data['warranty'],'\n\n')
    print('Model: ', obj.dell_data['sysconfig']['model'])
    print('Country: ', obj.dell_data['sysconfig']['country'])

    for i in obj.dell_data['sysconfig']['components']:
        for k, v in i.items():
            print(k,': ', v)

def SingleQueryTest():
    '''Test the main class'''
    try:
        obj = scrapping.QueryOEM(PART_NUMBER=part_num)
        obj.get_from_dell()
    except BaseException as e:
        print(">> Error instantiating main Class: {0}".format(e))
        raise

    stdout(obj)

def MultiQueryTest():
    '''Test the wrapper'''
    try:
        obj = scrapping.MultipleQueryOEM([part_num])
        obj.get_from_dell()
    except BaseException as e:
        print(">> Error instantiating main Class: {0}".format(e))
        raise
    
    for query in obj.results:
        print(query.dell_data)


# Runs the test
MultiQueryTest()