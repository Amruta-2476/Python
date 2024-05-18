# 4) Length of following set is ?
'''s = set()
   s.add(20)
   s.add(20.0)
   s.add("20")
'''
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)    #OP -> {20, '20'}
print(len(s))   #OP -> 2

'''This is bcoz 20 and 20.0 are the same numbers, just
 their types are different i.e 20 is in int form,
 while 20.0 is still 20 but in float form'''