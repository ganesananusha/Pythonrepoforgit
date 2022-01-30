# from Dictexamples import *
# # append()	Adds an element at the end of the list
# # clear()	Removes all the elements from the list
#
# # count()	Returns the number of elements with the specified value
# # extend()	Add the elements of a list (or any iterable), to the end of the current list
# # index()	Returns the index of the first element with the specified value
# # insert()	Adds an element at the specified position
# # pop()	Removes the element at the specified position
# # remove()	Removes the first item with the specified value
# # reverse()	Reverses the order of the list
# # sort()	Sorts the list
#
# list1=[1,2,3,4,5,6,"aa",1,1,1,1,1,6]
# list1=["ab","bc","cd","op"]
# list1.append(7)
# print list1
# print list1.count(1)
# list2=[9,7,5,3]
# list1.extend(list2)
# print list1
# print list1 + list2
# print list1.index(6)
# list1.insert(10,99)
# print list1
# list1.pop(2)
# print list1
# list1.remove(1)
# print list1
# list1.sort()
# print list1
# list1.reverse()
# print list1

### slicing in lists
list2=[100,99,98,97,96,95,94,93,92,91,90]
# print list2[-1::]
# # print list2[4]
# print list2[::]
# print len(list2)
# print range(0,3)
# print list2[0]
# print list2[1]
# for var in range(len(list2)):
#     print var
#     print "list element is"
#     print list2[var]
# for a in range(len(list2)):
#     print list2[a]
print list2[1:3]
# print list2
# print list2[-1]
# print list2[::-1]
list3=["malayalam","poor","laypao"]
print type(list3)
print type(list3[0])
# print list3[0]
# st1=str(list3[0])
# print st1
# print type(st1)
# st1="mala"
# print st1
# print type(st1)
# list4=list(st1)
# print list4
# print type(list4)


rows = [ ['Nikhil', 'COE', 2, '9.0'],
         ['Sanchit', 'COE', '2', '9.1'],
         ['Aditya', 'IT', '2', '9.3'],
         ['Sagar', 'SE', '1', '9.5'],
         ['Prateek', 'MCE', '3', '7.8'],
         ['Sahil', 'EP', '2', '9.1',[0,9]]]
print rows[5][4][1]
rows[0]="Anusha"
print rows
