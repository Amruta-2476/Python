myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white"],
  "anotherDict": {"name":"Amruta", "age":19}
}

# copy a dict using .copy() method
original = {1:'geeks', 2:'for'}
new = original.copy() 
original[1] = "GEEKS"
print(original)
print(new)
# modifications to original does not impact new