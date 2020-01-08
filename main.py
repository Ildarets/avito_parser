from class_Href_Model import Href_Model
from class_list_models import List_Models
from class_Deep_Parser import Deep_Parser
import pprint

# href_BMV = Href_Model('bmw', 10)
#
# print(href_BMV.href_models())
# print(len(href_BMV.href_models()))
# pprint.pprint(href_BMV.href_models())
#
# list_models = List_Models()
# pprint.pprint(list_models.list_models())

param = Deep_Parser('ferrari_360_2000_1775773846')
pprint.pprint(param.parsing())