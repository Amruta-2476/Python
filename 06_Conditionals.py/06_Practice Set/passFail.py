# 2) WAP to find pass/fail if it requires total 40% and atleast 35% in each of the 3 subjects to pass
 
sub1 = int(input("Enter marks for sub1: "))
sub2 = int(input("Enter marks for sub2: "))
sub3 = int(input("Enter marks for sub3: "))

if(sub1<35 or sub2<35 or sub3<35):
    print("Sorry...You failed.")

elif((sub1+sub2+sub3)/3) <40:
    print("You failed as total is less than 40")

else:
    print("Yay! You have passed the test.")