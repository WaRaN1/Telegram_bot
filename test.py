# my_dict = {'key': 1}
# print(my_dict)
# my_dict.update({'another_key': 2})  # Дополняем.
# print(my_dict)
# my_dict.update({'another_key': my_dict["another_key"] + 5})  # Обновляем.
# print(my_dict)
import os
import json


a = {"1": {"1": 2}}
x = {"1": 2}
for i in a:
    print(a[i])
    if x == a[i]:
        print("Yes")
    else:
        print("No")