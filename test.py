# my_dict = {'key': 1}
# print(my_dict)
# my_dict.update({'another_key': 2})  # Дополняем.
# print(my_dict)
# my_dict.update({'another_key': my_dict["another_key"] + 5})  # Обновляем.
# print(my_dict)


var = {"1078434603": {"Вода 0.5": "13", "Вода 1.5": "25", "Печиво \"Олімпія\"": "25"}}
for i in var["1078434603"]:
    print(i)
    print(var["1078434603"][i])