from Deep_parser import Deep_Parser
import pprint
import time
import json

FROM = 488
TO = None
MARK_NAME = 'nissan'

with open(f'list_href_cars_{MARK_NAME}.json', 'r') as f:
    result = json.load(f)
    pprint.pprint(result)

list_cars_href = result[FROM : TO]


NAME_FILE = f'cars_params_{MARK_NAME}.json'
parametrs_cars = []
def write_json(cars_dict):
    try:
        data = json.load(open(NAME_FILE))
    except:
        data = []
    data.append(cars_dict)
    with open(NAME_FILE, 'w') as file:
        json.dump(data, file, ensure_ascii=False)
#
for href_model in list_cars_href:
    time.sleep(1)
    try:
        params = Deep_Parser(href_model)
        car_params = params.parsing()
        parametrs_cars.append(car_params)
        pprint.pprint(car_params)
        write_json(car_params)
    except:
        time.sleep(60)


