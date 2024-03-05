f = open('sample2.txt', 'a')
f.write('Now this file has more content due to append&read.py')
f.close()

# open and read file after append
f = open('sample2.txt')
data = f.read()
print(data)