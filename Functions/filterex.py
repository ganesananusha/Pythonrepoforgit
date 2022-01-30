def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# value=fun('b')
# if value:
#     print "It is a vowel"
# using filter function
filtered = filter(fun, sequence)
print filtered
print('The filtered letters are:')
for s in filtered:
    print(s)