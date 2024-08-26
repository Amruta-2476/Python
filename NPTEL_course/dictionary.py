con_fact = {}
con_fact['dollar'] = 0.012
con_fact['euro'] = 71
con_fact['yen'] = 60
print(con_fact)

del con_fact['euro']
print(con_fact)

print(con_fact.keys())
print(con_fact.values())

rupees = int(input("Enter the amount in rupees: "))
rupees = rupees*con_fact['dollar']
print(round(rupees, 2))


