with open('sampleWith.txt', 'r') as f:
    data = f.read()
with open('sampleWith.txt', 'w') as f:
    data = f.write('this is write function')
print(data)