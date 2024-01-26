# 2) WAP to fill in a letter template given with name and date
# letter = 
'''Dear <|NAME|>
         You are selected !
   Date: <|DATE|>'''

name = input("Enter your name: ")
date = input("Enter date: ")

letter = '''Dear <|NAME|>, \n\tGreetings from XYZ. \n\tI am happy to tell you that, you are selected ! \nDate: <|DATE|>'''

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)