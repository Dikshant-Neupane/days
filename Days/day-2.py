########## Remove specified items form a set
# mylist=["apple","banana","cat","ssddwd"]
# # # mylist.pop(2)
# # del mylist[0]
# # del mylist is used to delet completely 
# mylist.clear() #is taken is use so that content only gets erased 
# # mylist.remove("cat")
# print(mylist)
    ############     Loop through a list
     
# for x in mylist:
#     print(x) #yesle garda list aba queue ma arrange hunxa
    
# for i in range(len(mylist)):
#   print(mylist) # yesle garda chai jati ota content xa teti choti nai print hunxa
  
  
  
# i=0
# while i< len(mylist):
#     print(mylist)
#     i=i+1  #same mathi ko jastai jati ota xa content teti choti print bhayera auxa



# ####################  list comprehensive
    
# newlist=[]
# for x in mylist:
#     if"a" in x:
#         newlist.append(x)
#         print(newlist)
    
#     #aba yesslie directly comprehensive way ma kasari garne?
# newlist=[x for x in mylist if "a" in x] 
# print(newlist)
#     

################ Condition

# 
# # yesh  ko lagi simple syantax bhanko newlist=[expression for item in iterable if condition ===True]


# #example
# newlist=[x for x in mylist if x!="apple"]
# print(newlist)
#     #this ablove code removes the apple from the set
    
    
    
# newlist=[x for x in range(10) if x<3]
# print(newlist)


# newlist=[x.upper( ) for x in mylist]
# print(newlist)

############### sort used to sort aplhanumerically

# mylist.sort()
# print(mylist)


# list=[10,30,1,2,40,22]
# list.sort(reverse=True)
# # list.sort()
# print(list)


############## Customize sort formation

# def myfunc(n):
#     return abs(n-50)
# list=[10,2,3,41233,43]
# list.sort(key=myfunc) # This sorts based on each number's distance from 50
# print(list)
# # Output: [43, 10, 3, 2, 41233]
# # 43 comes first because |43-50|=7 (closest to 50)
# # 41233 comes last because |41233-50|=41183 (furthest from 50)


########### to arrange sort in case insensitive using key=str.lower or upper
# mylist=["abc","Bcd","ade","Ada"]
# # # mylist.sort(key=str.upper)
# # print(mylist)  # Output: ['abc', 'Ada', 'ade', 'Bcd'] upppercase ly sorrt garyo
# copylist=mylist.copy()   ### another way to copy a list is by assigning copylist=list(mylist)
# print(copylist)
# thislist=mylist[:] ###  : ly slice operator bhaninxa yesko use garera pani copy garna milxa
# print(thislist)

################ JOinig list
# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1 + list2
# print(list3)

###another way to join a list is my apppending
# list1=["a","b","c"]
# list2=[1,2,3]
# # for x in list2:
# #     list1.append(x)  # Append the current item from list2 
    
# # print(list1)
#  #########  axtend to use garera pani join garna milxa
# list1.extend(list2)
# print(list1)




#########################  TUPLE (unchange able list)

# tuplelist=("apple","banana","cat","apple")##it allows duplicates
# # print(tuplelist)
# print(len(tuplelist))#lenght herna 
#  #tupple cannot be created with one item but....
# list=("aple",)
# print(type(list))
 
####### aother way to declare a tuple

# list=tuple(("appple",))##rember it have two inclosed brackets 
# print(list)
###smilar to list we can access tuple items
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])


# ############### Updates the tuples

# x=("apple","orange","banana")#here new variable y is introduced as a temp variable we can perform any change in tuple as tuple cant be manupuated directly
# y=list(x)
# y[1]="kiwi"
# x=tuple(y)
# print(x)  



###add items y=list(x)
# x=("apple","orange","banana")
# y=list(x)
# y.append("kiwi")
# x=tuple(y)
# print(x)


###############Add typle to tulpe
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


############ Remove a tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#del thistuple garesi sabai tuple nai udxa