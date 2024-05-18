# for i in range(start, stop, stepSize):

for x in range(6):
  print(x)
# 6 is excluded

print("")
for x in range(2, 6):
  print(x)

print("")
# skip/step count by 3
for x in range(2, 20, 3):
  print(x)

print("")
for x in range(6):
  if x == 3: 
    break
  print(x)
else:
  print("Finally finished!")