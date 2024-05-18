# 9) WAP to print following:
'''
* * *
*   *
* * *      for n=3'''
n=3
for i in range(n):
    if  i == 0 or i == n - 1:
        print('* ' * n)
    else:
        print('*' * (n-2)+"   *")

# check this please