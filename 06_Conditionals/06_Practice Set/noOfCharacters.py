# 4) WAP to find whether a given username contains less than 10 characters
username = input("Enter your username: ")
if len(username) < 10:
    print("Alert! Username has less than 10 characters.")
else:
    print("Welcome",username)