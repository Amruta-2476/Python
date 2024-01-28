#  dict is ordered and changeable, doesn't allow duplicates
myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white"],
  "anotherDict": {"name":"Amruta", "age":19}
}
print(myDict)

print("")
# Access values in dictionary using their keys
print("Brand: ",myDict["brand"])
print("Color options: ",myDict["colors"])
print("Dict inside myDict: ",myDict["anotherDict"])
print("Name from Dict inside myDict: ",myDict["anotherDict"]["name"])


# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print("")
# changing values of myDict
print("Before changing value: ",myDict)
myDict["colors"] = ["red", "white", "black", "blue"]
print("After changing value: ",myDict)