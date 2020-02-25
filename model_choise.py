from class_list_models import List_Models

models = List_Models()
list_models = models.list_models()

for id, item in enumerate(list_models):
    print(id, item)

for model in list_models[66]:
    print(model)
