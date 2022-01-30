data1=["['Question1. The buying or selling of goods over the internet is termed as\\n', '(1) e-selling\\n', '(2) e-buying\\n', '(3) e-business\\n', '(4) e-commerce\\n']"]
data2=[]
for data in data1:
    # print data
    print type(data)
    data2.append(data.split(","))
# print data2
    for final in data2:
        data3= final
        print data3[:-3]
    #  print data3