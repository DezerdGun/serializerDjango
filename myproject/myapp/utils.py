import json
import os
from django.conf import settings

FILE_PATH =  os.path.join(os.path.dirname(__file__),'data.json')

def read_data():
    with open(FILE_PATH,'r') as file:
        return json.load(file)
    
def write_data(data):
    with open(FILE_PATH,'w') as file:
        json.dump(data,file,indent=4)   