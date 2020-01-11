from class_Href_Model import Href_Model
from class_list_models import List_Models
from Deep_parser import Deep_Parser
import pprint
import time
import json

parametrs_cars = []
list_models = List_Models()
all_list_models = list_models.list_models()

non_duplicate = list(set(all_list_models))
all_list_models = non_duplicate


def write_json(cars_dict):
    try:
        data = json.load(open('cars_params_dict1.json'))
    except:
        data = []
    data.append(car_params)
    with open('cars_params_dict1.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False)


# car = {}
# with open ('parametrs_cars8.json', 'w') as f:
#     json.dump(car,f)

# #РАбочй код
for model in all_list_models[0:22]:
    href_BMV = Href_Model(model, 2)
    list_cars_href = href_BMV.href_models()
    # print(href_BMV.href_models())
    print(len(list_cars_href))
    pprint.pprint(list_cars_href)
    try:
        for href_model in list_cars_href:
            # print(href_model)
            time.sleep(0.5)
            params = Deep_Parser(href_model)
            car_params = params.parsing()
            parametrs_cars.append(car_params)
            # with open('parametrs_cars9.json', 'a') as f:
            #     json.dump(car_params, f)
            pprint.pprint(car_params)
            write_json(car_params)
    except:
        time.sleep(60)
# pprint.pprint(parametrs_cars)

# with open ('parametrs_cars_list9.json', 'w', encoding='utf-8') as f:
#     json.dump(parametrs_cars,f)

# param = Deep_Parser('/krasnoyarsk/avtomobili/ford_taurus_1992_1800191092')
# pprint.pprint(param.parsing())
