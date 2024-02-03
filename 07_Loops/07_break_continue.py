# break: stops loop exeution when condition occurs
i = 1
while i < 10:
  print(i)
  if i == 7:
    break
  i += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("")
# continue: stops the current iteration and continues with next iteration
i = 0
while i < 10:
  i += 1
  if i == 3:
    continue
  print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)