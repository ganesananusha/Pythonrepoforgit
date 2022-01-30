from time import *
import pyodbc
sleep(1)
clock()


# #
# ##
# ###
# ####
# #####
# ######
# #######
# ########
# #########
# ##########
#Print the above pattern
string1="#"
print string1
for i in range(1,10):
    print string1+ string1*i

# Program 2
#
# 1
# 1 2
# 1 2 3

for i in range(1,12):
    data= range(0,i)
    print data

rows = 10
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print column,
    print " "





