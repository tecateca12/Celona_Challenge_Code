"""
Ezequiel Celona QA Engineer - code challenge
Date: 3/15/2021
Contact: tecateca12@gmail.com
"""

import unittest

# Define constants
CONSTS = {
    'valueError': ValueError('Invalid argument type'),
    'valueTypes': [int,float]
    }

# Define Test data
TEST_SET = {
    'strings': [
        {'value':'etete','outcome':True},
        {'value':"ETetE", 'outcome': True},
        {'value':"Tester", 'outcome': False},
        {'value':"ab ba", 'outcome': True},
        {'value': 1500, 'outcome': CONSTS['valueError']},
        {'value':[1,2],'outcome': CONSTS['valueError']},
        {'value':{'test':'test'},'outcome': CONSTS['valueError']},
        {'value' :True, 'outcome': CONSTS['valueError']},
        {'value': object,'outcome': CONSTS['valueError']},
        {'value': ['test'], 'outcome': CONSTS['valueError']},
    ],
    'array':[
       {'value': [0,1,2,0,3], 'outcome': [1,2,3,0,0]},
       {'value': [0.1,2,0,4,4,10000,0.0, 5000.55], 'outcome': [0.1,2,4,4,10000,5000.55,0,0.0]},
       {'value': [], 'outcome': []},
       {'value': [[]], 'outcome': CONSTS['valueError']},
       {'value': [[0,1,2]], 'outcome': CONSTS['valueError']},
       {'value': [0,"1",2], 'outcome': CONSTS['valueError']},
       {'value': True, 'outcome': CONSTS['valueError']},
       {'value':(1,0,2,3), 'outcome': CONSTS['valueError']}
    ]
}

def is_palindrome(arg):
    """
    :param arg: str
    :return: Boolean or Value error if param type is wrong
    """
    aux = lambda s: True if str(s) == str(s)[::-1] else False
    if type(arg) is str:
        return aux(arg.lower())
    else:
        return CONSTS['valueError']

def sort_zeros(array):
    """
    :param array: list
    :return: normalized list or Value error if arg type is wrong
    """
    def normalize(aux,array):
        [array.pop(array.index(x)) for x in array if x == 0]
        array.extend(aux)
        return array
    if type(array) is not list:
        return CONSTS['valueError']
    aux = []
    for x in array:
            if type(x) in (CONSTS['valueTypes']):
                (aux.append(x)) if x == 0 else None
            else:
                return CONSTS['valueError']
    return normalize(aux,array)

class testClass(unittest.TestCase):
    def testPalindromeHappyPaths(self):
        for case in TEST_SET['strings']:
            try:
                self.assertTrue(is_palindrome(case['value']) == case['outcome'])
            except Exception as e:
                raise e

    def testArraySorter(self):
        for case in TEST_SET['array']:
            try:
                self.assertTrue(sort_zeros(case['value']) == case['outcome'])
            except Exception as e:
                raise e

if __name__ == '__main__':
    unittest.main()