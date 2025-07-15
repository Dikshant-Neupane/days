# dis={
#     "brand":"ford",
#     "model":"mustang"
# }
# dis.update({"color":"red"})
# # print(dis)
# dis.pop("color")#pop use garsi delet hunxa
# print(dis)
# # also we can use popitem( ) for version 3.7 and before version



###### to delet an item we can also use del() as set,tuple and list
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict) ### usig clear clears all all the set 


# loop in dictonary is similar to that of list,tuples and set
# for  x in thisdict.values():
#     print(x)
    
    
    ### also a popular and most effective way is to use key() and items()
    # for x in thisdict.keys():
    #     for x in thisdict.items():
    
    ####copy()  and dict() functions can also be used to make the copy of the existing dictonary
    
    
    
    
    
    
    
    ##################### NESTED Dictionaries
    
# myfamily={
#         "child1":{
#             "name":"dikshant",
#             "year":"2000"
#         },
#         "child2":{
#             "name":"Neupane",
#             "year":"2001"
#         }
        
#     }
# print(myfamily)


## creating three dictionary then creating one dictionary that wull conatin the other three dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
# print(myfamily)
# print(myfamily["child2"]["name"])###this prints the name stored in child2 dictionary 


########## Loop in nested dictioanry

for x, obj in myfamily.items():###obj complier le afai xa bhanera ani afaiii assume garxa
  print(x)

  for y in obj:
    print(y + ':', obj[y])