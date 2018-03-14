import json
from flask import request
import re

def filter_regex(criteria):

    elements = json.loads(request.data)
    elements_found = []
    p = re.compile(criteria)
    print(p)
    for elem in elements['elements'].split(' '):
        print(elem)
        if p.match(elem):
            print("matched")
            elements_found.append(elem)
        			
    return elements_found

