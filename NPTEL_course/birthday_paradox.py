# find duplicate birthdays 

import random 
birthday = []
i = 0 
while(i<400):
    year = random.randint(1990, 2012)
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        # print("Leap year",year)
        leap = 1
    else:
        # print("not leap year",year)
        leap = 0
    month = random.randint(1,12)
    
    if (month == 2 and leap == 1):
        day = random.randint(1,29)
    elif (month ==2 and leap == 0):
        day = random.randint(1,28)
    elif month in [1,3,5,7,8,10,12]:
        day = random.randint(1,31)
    else:
        day = random.randint(1,30)
    birthday.append(f'{day}/{month}/{year}')
    i = i + 1
    
same_bday = set()   # this is how u define empty set ;set to avoid the double entry into same_bday 
for i in range(len(birthday)):             # used logic from sorting algo
    for j in range(i+1, len(birthday)):
        if (birthday[i] == birthday[j]):
            same_bday.add(birthday[i])
    
for bday in same_bday:
    print(bday)
    

    