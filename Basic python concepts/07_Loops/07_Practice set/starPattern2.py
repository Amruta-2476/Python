# 8) WAP to print this for n=3
'''
*
** 
***  
****  '''
n = int(input("Enter a number: "))
for i in range(n+1):
    for j in range(1, i+1):
        # print("* ")
        print("*", end=" ")  #this end=" " is needed coz by default it is \n
    print()