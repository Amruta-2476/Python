# refer: https://www.geeksforgeeks.org/magic-square/
def magicSquare(n):
    matrix = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(0)
        matrix.append(r)
    # for i in range(n):
    #     for j in range(n):
    #         print(matrix[i][j], end=' ')
    #     print()  
    
    #this will print nxn matrix with all 0s
    
    i = n//2  # floor division to make i and j integers
    j = n-1
    num = n*n
    count = 1
    while(count <= num):
        if (i == -1 and j == n):  # 3rd condition
            j = n-2
            i = 0
        else:
            if j == n: # 1st condition
                j = 0
            if i < 0:  # 1st condition
                i = n-1
        if (matrix[i][j] != 0):
            j = j-2
            i = i+1
            continue
        else:
            matrix[i][j] = count
            count += 1
        i = i-1
        j = j+1  # 1st condition
    
    for i in range(n):
         for j in range(n):
             print(matrix[i][j], end=' ')
         print() 
         
    print("The sum of each row/column/diagonal is: " + str(n*(n**2+1)/2))
magicSquare(3)