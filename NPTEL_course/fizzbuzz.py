# numbers 1 to 20. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

for i in range(1, 21):
    # print(i, end = ' ')
    # if (i % 3 == 0 and i % 5 == 0):
    #     print(f'{i} = FizzBuzz')
    # elif (i % 3 == 0):
    #     print(f'{i} = Fizz')
    # elif (i % 5 == 0):
    #     print(f'{i} = Buzz')
    # else:
    #     print(i)
    if (i % 3 == 0):
        print(f'{i} = Fizz')
        if ( i % 5 == 0):
            print(f'{i} = FizzBuzz')
    elif (i % 5 == 0):
        print(f'{i} = Buzz')
    else:
        print(i)