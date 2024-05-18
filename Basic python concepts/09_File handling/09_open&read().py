'''f = open("sample.txt")'''
# this is same as this:
'''f = open("sample.txt", "rt")'''
# coz "r" for read, and "t" for text are the default values, you do not need to specify them.

# OPEN FUNCTION TO READ THE CONTENT OF A FILE
f = open('sample.txt', 'r')
# data = f.read()
# print(data)  # op = The Earth revolves around the Sun
fewDAta = f.read(6)
print(fewDAta)  # op = The Ea
f.close()

# if file located in different location 
'''f = open("D:\\myfiles\sample.txt", "r")
print(f.read())'''