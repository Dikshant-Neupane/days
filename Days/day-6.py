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
    
myfamily={
        "child1":{
            "name":"dikshant",
            "year":"2000"
        },
        "child2":{
            "name":"Neupane",
            "year":"2001"
        }
        
    }
print(myfamily)