import math
import time

# device ={"four" :"scanner","three":"printer","one":"mouse","nine":"monitor"}
# for i in device:
#     print device[i]
# for length in range(len(device)):
#     print device[length]


dict_create={}
dict_create1=dict()
dict_create["student1"] = "Aditya"
dict_create["strdent2"] = "Aparna"
# print dict_create
print dict_create.values()
print dict_create.keys()
print dict_create.items()
print len(dict_create.items())
list1=[1,2,3,4,[5,6,7]]
print list1[4]
print dict_create.items()[0][1]
print type(dict_create.items()[0])
print dict_create.get("student1")
print dict_create.get("aaaa")
dict_create.update(device)
#
print dict_create
print dict_create.pop("one")
print dict_create
dict_create.popitem()
print dict_create
# dict_create.update({"test":"data"})
# print dict_create
for key, value in dict_create.items():
    print (key ,'-----' ,value)
