import random

year = random.randint(1990, 2012)
# year = 1900 # 1900 is not a leap year, hence we need the 100 condition
print(year)
# check if leap year
if (year % 400 == 0):
    print("Leap year")
elif(year % 100 == 0):
    print("Not a leap year")
elif(year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")


month = random.randint(1, 12)
print(month)
if month == 2:
    # if (year % 400 == 0):
    #     print("29 days")
    # elif(year % 100 == 0):
    #     print("28 days")
    # elif(year % 4 == 0):
    #     print("29 days")
    # else:
    #     print("28 days")     # better way to do this is
    if ( year % 400 == 0 or (year%4 == 0 and year%100 != 0)):
        # print("29 days")
        day = random.randint(1, 29)
    else:
        # print("28 days")
        day = random.randint(1, 28)

elif month in [1, 3, 5, 7, 8, 10, 12]:
    # print("31 days")
    day = random.randint(1, 31)
else:
    # print("30 days")
    day = random.randint(1, 30)


print(f'{day}/{month}/{year}')