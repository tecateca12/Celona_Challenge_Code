# Ezequiel Celona Code challenge

## Quickstart

### Requirements
- Python 3 (developed and tested under v 3.6.9)
- Git

### Deployment
To deploy the tool:
1. Clone the repository
2. On terminal navigate to root folder

```
python test.py
````
- Note: since there is no external libraries nor dependencies there is no needed to create a virtualenv, just be sure that your code is running under python3 version.

### Test Data
Unit tests and test data for both developed methods are included on the same *.py* file.

```
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

```

