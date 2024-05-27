# Find the output of the following program.
String = 'Welcome to Engineering session'
# slice(start, end, step)
s1 = slice (3)
s2 = slice (1,6,2)
print (String[s1])    # Wel ==> index 0 to index 3 (exclusive)
print (String[s2])    # ecm
print (String [0:8])  # Welcome
print (String [0:10:1])  # Welcome to ==>step of 1 (default)
print (String [0:30:2])  # Wloet niern eso
print (String [0:7:3])   # Wce
print (String [-7: -2])  # sessi  ==> index -2 excluded
print (String [-7: -1:2])   #ssi
print (String[::-1])  #noisses gnireenignE ot emocleW
print ("String slicing")
