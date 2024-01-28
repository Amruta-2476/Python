# Dictionary methods: 

# can access values by using .get() too
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get("model"))
print(thisdict["model"])
# both do the same thing: but if we write "model2"

# print(thisdict.get("model2"))  #None
# print(thisdict["model2"])  # keyError 
# .get() returns None if the key is not in the dictionary, while [] will raise a KeyError. Coz when you give key in a square bracket, then it's your responsibility to make sure that the key exists in the dictionary. 


# 1) get list of all keys using .keys()
print(thisdict.keys())        # dict_keys(['brand', 'model', 'year'])
print(type(thisdict.keys()))   # <class 'dict_keys'>
print(list(thisdict.keys()))   # ['brand', 'model', 'year']

# 2) get list of all values using .values()
print(thisdict.values())

# 3) print (key,value) for all items using .items()
print(thisdict.items())       # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# check if a key exists in the dictionary, use .has_key() or just 'in' keyword
print("color" in thisdict)

# add new item to see change in keys() and values()
thisdict["color"]="red"
print(thisdict.keys())
print(thisdict.values())

# 4) .update()
newDict = {
    "raceCar": False
}
thisdict.update(newDict)
print(thisdict)