# DICTIONARY

# thislist={
#     "brand":"ford",
#     "model":"mustang"
    
# }
# print(thislist)


# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# Accessing the dictonary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# or x = thisdict.get("model")
print(x)

# get keys
x = thisdict.keys()
print(x) #indicates all the key values from dictonary


# Add new item in the dictonary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change