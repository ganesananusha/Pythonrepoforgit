import random
print random.randint(0,2)
print random.randrange(0,2)
def Myfunc():
    global tigers
    tigers ="anusha"
    print tigers

### main
tigers = "vishwa"
print tigers
Myfunc()
print " after global scropr "
print tigers