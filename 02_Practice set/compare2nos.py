# 4) WAP TO COMPARE 2 NOS. USING COMPARISON OPERATOR
a= input("enter numm1:")
a=int(a)
print(a)

b= input("enter numm2:")
b=int(b)
print(b)

print(a>b) #will print true/false

# OR USING IF_ELSE
if (a>b):
    # print(a + " is greater") this is wrong

    # IN JAVA WE WRITE System.out.println(a+" is greater");
	# SIMILARLY IN C WE WRITE printf ("%d is greater”, a);
	# HERE'S AN EQUIVALENT EXAMPLE IN PYTHON:
    print("a = {} is greater".format(a))

else:
    print("b = {} is greater".format(b))