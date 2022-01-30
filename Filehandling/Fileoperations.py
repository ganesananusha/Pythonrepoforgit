
import random
list=[]
for i in range(5):
    r=random.randint(1,20)
    if r not in list:
        list.append(r)
print list
fileopen = open("urllist.txt","r")
readdata=fileopen.readlines()
filewrite=open("question.txt","a")
filewrite = open(r'C:\Users\ag\PycharmProjects\Vishwa\samplefile.txt','w')
for j in range(len(list)):
    print readdata[list[j]]
    filewrite.write(readdata[list[j]])
filewrite.close()
contents = open(r'C:\Users\ag\PycharmProjects\Vishwa\samplefile.txt',"r")
with open("samplequestions.html", "w") as e:
    for lines in contents.readlines():
        e.write("<pre>" + lines + "</pre> <br>\n")


### Input : Enter the Master Question file name :
#Enter the number of questions needed
# Enter the output Question pare file name



### use read , readline , readlines
## find the type of return value


