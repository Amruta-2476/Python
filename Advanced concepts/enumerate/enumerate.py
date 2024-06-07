list = [3, 5, 'yo', True]
for item in list:
    print(item, end=' ')
    print(list.index(item))
# Output:
'''3 0
5 1
yo 2
True 3'''

# OR : enumerate() adds counter to index and returns it 
for index, item in enumerate(list):
    print(item, index)