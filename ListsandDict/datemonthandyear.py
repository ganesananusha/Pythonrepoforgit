# a=12232020
# print a%10000
# daymonth=a/10000
# month=daymonth/100
# print month
# day=daymonth%100
# print day
#
# stime = input("Enter start time : ")
# print(stime)
# endtime = input("Enter end time :")

#
#
# stime ="0900"
# endtime="1730"
# sub= int(endtime) - int(stime)
# print str(sub/100)+"hours"
# if sub %100 <=59:
#     print str(sub%100) +"minutes"

month={"January":1,"February":2,"March":3,"April":4,"May":5}
days31=[1,3,5,7,8,10,12]
print month.values()
# tofindmonth= input("enter month :")
# # print month.find(tofindmonth)
# # print month.has_key(tofindmonth)
# # print tofindmonth in month
# monthnu= month[tofindmonth]
# if monthnu ==2:
#     print 28
# elif monthnu in days31:
#     print 31
# else:
#     print 30
monthtoget = int(input("enter month number:"))
for key,value in month.items():
    # print k
    # print v
    if value==monthtoget:
        print key
