# Create a Python program that performs a binary search on a sorted list of integers using only loops. The program should prompt the user to input a sorted list of integers and a target number to search for. The program should then search for the target number in the list using the binary search algorithm and print the index of the target if found. If the target is not found, the program should print -1.

# The first line of input consists of a space-separated sorted list of integers.
# The second line of input consists of a single integer, representing the target number.
# Output Format:

# The output consists of the index of the target number in the list if found. If the target number is not found, the output should be -1.

# Input:
# 10 20 30 40 50
# 30

# Output:2


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (high + low) // 2
        if sorted_list[mid] == target:
            return mid  
        elif sorted_list[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  
            
    return -1 

input_str = input().split()
sorted_list = []
for item in input_str:
    sorted_list.append(int(item))

target = int(input())

result = binary_search(sorted_list, target)
print(result)




# When you type list of numbers (e.g., "10 20 30 40 50"), it's initially a single string.
# hence we need to split is using input().split(). So, "10 20 30 40 50" becomes a list of strings: ["10", "20", "30", "40", "50"]. 
# Then we need to convert each string to an integer using int() function.
# So, we use a for loop to iterate over each string in the list and convert it to an integer.
# Finally, we append the integer to the sorted_list.
