from class_Href_Model import Href_Model
from class_list_models import List_Models
from Deep_parser import Deep_Parser
import pprint
import time
import json

count_mark = 2000
DEEP = int(count_mark / 54)
MARK_NAME = 'porsche'
NAME_FILE = f'cars_params_{MARK_NAME}.json'

parametrs_cars = []
list_models = List_Models()
all_list_models = list_models.list_models()

def write_json(cars_dict):
    try:
        data = json.load(open(NAME_FILE))
    except:
        data = []
    data.append(cars_dict)
    with open(NAME_FILE, 'w') as file:
        json.dump(data, file, ensure_ascii=False)

# #РАбочй код

href_BMV = Href_Model(MARK_NAME, DEEP)
list_cars_href = href_BMV.href_models()
print(len(list_cars_href))
for href_model in list_cars_href:
    time.sleep(0.7)
    try:
        params = Deep_Parser(href_model)
        car_params = params.parsing()
        parametrs_cars.append(car_params)
        pprint.pprint(car_params)
        write_json(car_params)
    except:
        time.sleep(30)

