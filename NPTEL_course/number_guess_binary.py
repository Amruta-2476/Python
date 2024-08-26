def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    flag = 0   # flag=0 means element not found
    count = 0  # count the number of iterations
    while (low <= high and flag == 0):
        count += 1
        mid = (low + high) // 2    # floor div to get int value
        if (arr[mid] == x):
            flag = 1
            print("Element found at index", mid)
            print("Number of iterations:", count)
            return
        else:
            if (arr[mid] < x):
                low = mid + 1
            else:
                high = mid - 1
    print("Element not found in the list")

a = []
for i in range(1, 100):
    a.append(i)

binary_search(a, 45)
    