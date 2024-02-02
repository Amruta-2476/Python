a = {1,2,3,4,5}  #<class 'set'>
print(a)
print(type(a))  
# Sets are unordered, so the items appear in random order.

# for duplicates
b= {1,2,3,5,1,2}
print(b)  #{1, 2, 3, 5}

# In set, True = 1   and   False = 0 so they are considered as duplicates
c = {True,False,1,0}  # -> {False, True}
#whichever is first in the set, gets printed
e = {1,0,True,False}  # -> {0, 1}
d = {True,False,"1","0"}  #these 1 and 0 are str
print(c)
print(e)
print(d)
