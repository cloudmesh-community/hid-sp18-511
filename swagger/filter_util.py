import json
from flask import request

def filter_negative():

    numbers = json.loads(request.data)
    numbers_neg = []
    
    for number in numbers['numbers'].split(' '):
        if int(number) < 0:
            numbers_neg.append(int(number))
        			
    return numbers_neg

def filter_positive():

    numbers = json.loads(request.data)
    numbers_pos = []
        
    for number in numbers['numbers'].split(' '):
        if int(number) >= 0:
            numbers_pos.append(int(number))
    			
    return numbers_pos
