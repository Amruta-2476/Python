def linear_search(n, x):
    element = []
    for i in range(1, 101):
        element.append(i)
    count = 0   # to count no.of iterations it takes to find
    flag = 0
    for i in element:
        count = count + 1
        if (i == x):
            print("Element found at position: ", i)
            flag = 1
            break   # to break loop if element is found, as no need to go through the rest of the elements. otherwie it will take 'n' iterations to find any element

    if (flag == 0):
        print("Element not found")

    print("No.of iterations it took to find the element: ", count)
linear_search(100, 55)


