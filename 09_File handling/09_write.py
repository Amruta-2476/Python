f = open('sample2.txt', 'w')
f.write('Harry Potter and the ')


f = open('sample2.txt', 'a')
f.write('Chamber of secrets')

f.close()  
#we didn't have to create a file, 'w' and 'a' mode create a new file if it doesn't already exist

