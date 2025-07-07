# fruits =["apple","banana","orange"]
# x , y , z = fruits
# print(x ,y ,z)

# x=5
# y=6
# print(x+y)

#                         # Global variable
# x ="aw3osome"
# def myfunc():
#     print("python is "+x)
    
# myfunc() 
 
 
#      #local and gobal varibles
# x="awosome"  
# # decleartion of global varibale
# def myfunc():
#     # function opens
#     x="fantastic"
#     # declaration of local varibale
#     print("Python is "+x)
# myfunc()
# # function close

# print("Python is "+x)     
    
# x="5"
# print(type(x))
        #complex number ko lagi type conversion
x=1
y=2.8
z=1j
 
#  convert from int to float 
a=float(x)
# convert from flot to int
b=int(y)

# convert from int to complex
# c=complex(x)

# print(a)
# print(b)
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))




########################import random numbe
# import random
# print(random.randrange(1,10))


# print('He is called "Johnny"')

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# LOOPING THROUGH STRING 

# for x in "banana":
# #   print(x)  

# #  a="banana"
# # print(len(a))
# txt="the best things in life are free!"
# print("free!" in txt) #xa bhane true auxa ouptt natra false auxa
# if "best" not in txt:
#     print("No experience is not present")


# #########################Slicing 
# b="Hello World!"
# print(b[2:])
# # h=0 testai llo=2,3,4  is only included and 5 is excluded


# #########################Uppper case
# a="     hello world    "
# print(a.upper())
# print(a.lower())
# print(a.strip()) #removes the space in the begining and ending of the string a

# #################Replace string 
# a="Hello World"
# print(a.replace("H","h"))
# a = "Hello, World!"
# print(a.split(",")) 


##########################   string concatenation
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)



# age = 20
# txt = "My name is dikshant, I am " + str(age) + " years old"
# print(txt)




################# F-string

# age=20
# txt= f"My name is dikshant I am {age} years old."
# print(txt)


# ########## Place holder
# price=59
# # txt=f"The price is {price:.2f} dollars"
# # txt=f"Theprce in dollar in ruppper is {price*90}"
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)



##################### Booleans
# # print(10>9)

# a=200
# b=33
# if b>a:
#     print("b is the greatest")
# else:
#     print("a is the greatest") 

# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))


# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))


# def myFunction() :
#   return True




# to print ys when true and no for false  
# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

# check if its intger or not
# x = 200
# print(isinstance(x, int))




##########################   Operators
#  x is y returns true if x=y
# x is not y returns ture if x doesnt equals to y




# ##################   List

# mylist =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist)
# print(len(mylist))
# print(type(mylist))
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:4])
# print(mylist[2:])
# print(mylist[-4:-1])
                        ###########333  chnage the list items
# mylist=["apple","banana","cat","dog","eye"]
# # mylist[1:3]=["zero ","herp","piro"]
# # mylist.append("zero")
# # mylist.insert(0,"zero")
# # mylist[0]="zero"
# print(mylist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
