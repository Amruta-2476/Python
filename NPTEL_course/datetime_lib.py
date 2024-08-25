import datetime
# todays date
today = datetime.date.today()
print(today)

# current year
print(datetime.date.today().year)  #or
print(datetime.date.today().strftime("%Y"))

# current month
print(datetime.date.today().month)  #or
print(datetime.date.today().strftime("%m"))

# current day
print(datetime.date.today().day)  #or
print(datetime.date.today().strftime("%d"))

# current weekday
print(datetime.date.today().strftime("%w"))

print("weak number of the year: ", datetime.date.today().strftime("%W"))

print("day of the year: ", datetime.date.today().strftime("%j"))

print("day of the week: ", datetime.date.today().strftime("%A"))