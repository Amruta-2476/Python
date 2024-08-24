# l0 = [9,3,5,1,12,9.6]
# l0.sort()
# print(l0)
# size = len(l0)
# print(f'2nd smallest is {l0[size-2]}')

size = int(input("ENTER size: "))
list1 = []
for i in range(size):
    el = int(input("ENTER: "))
    list1.append(el)
list1.sort()
print(list1)
# size = len(list1)
print(f'2nd largest is {list1[size-2]}')











# L = input().split(' ')
# L_int = []  
# for num in L:
#     L_int.append(int(num))  # Convert each string to an integer and append to the new list
# L = L_int 
# L = list(set(L))
# L.sort()
# print(L[len(L)-2])
#  ==>  https://chatgpt.com/c/e2005ff2-7949-4ea5-ad6a-802ec9a1348f


L = input().split(' ')
for x in L:
  if x in L[L.index(x)+1:]:
    del L[L.index(x, L.index(x)+1)]
print(' '.join( L), end='')


L = input().split(' ')
L = [int(num) for num in L]
l = []
for i in range(len(L)):
  if i % 2:
    l += [L[i] + L[-(i+1)]]
  else:
    l += [L[i]]
print(' '.join(map(str,l)), end='')