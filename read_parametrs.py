import json
import pprint
with open('cars_params_dict1.json', 'r') as f:
    result = json.load(f)
    # pprint.pprint(result)


# with open('parametrs_cars_list8.json', 'r') as f:
#     result = json.load(f)
#     pprint.pprint(result)

# f = open('parametrs_cars2.json')
# for line in f:
#     pprint.pprint(line)

# with open('parametrs_cars8.json', 'r') as f:
#     result = json.load(f)
#     pprint.pprint(result)
print(len(result))
for i in range(len(result)):
    x = result[i]['price']
    pprint.pprint(x)
    #
# print(len(result))
# pp = json.loads(result)
# for i in range(len(result)):
#     # pprint.pprint(result[i]['price'])
#     # print(result[i]['price'])
#     # x = result[i]['Марка']
#     # print(x)
#     x = result[i]['Марка'] = 'Mazda'
#     print(len(x))
#

