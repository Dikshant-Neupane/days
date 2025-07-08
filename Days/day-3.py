# ########  UNPACKING Tuples

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# ############## Using asterik **

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)#gets apple as its the first 
# print(yellow)#gets banana
# print(red)###gets all the remaining elements


# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits#when * is at the middle

# print(green)#gets the first one
# print(tropic)#remaining
# # print(red)#gets the last one


# ########## LOOPS in tuples
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# for x in fruits :
#     print(x)###prints the output in queue

# for i in range(len(fruits)):
#     print(fruits[i])

############  Using While LOOPS
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i=i+1


################ JOINING TUPLES

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)


# ################################## SETS
# myset={"apple","banana","cat"}
# print(myset)


# #Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)

# True and 1 is considered the same value:
# is already sorted


# print(len(thisset))
# myset = {"apple", "banana", "cherry"}
# print(type(myset))



# ###### CHecking is banana is in the set
# thisset = {"apple", "banana", "cherry"}

# # print("banana" in thisset)

# ###To add any item in the exisiting set 
# thisset.add("orange")
# print(thisset)


# ############# To add one set into another and make i one set

# tropical={"pineapple"}
# thisset.update(tropical)
# print(thisset)




############# Removing banana from the set
# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)


###Removing usinf discard( )Note: If the item to remove does not exist, discard() will NOT raise an error.
# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)

####### also You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)


####### to complete remove set / delet the set del setname

# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset)###whole se is deleted so no output



# ############Loop in set
# fruits={"apple","banana",'"cat'}
# for s in fruits:
#     print(s)