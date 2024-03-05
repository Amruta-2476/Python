# 1) WAP to read the text from a given file 'poems.txt' and fnd out whether it contains the word 'twinkle' or not?
f = open('poems.txt')
data = f.read()
print(data)
if 'twinkle' in data:
    print("twinkle found")
else:
    print("twinkle not found")
f.close()

