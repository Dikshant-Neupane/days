## Python Match
# #an alternative of if else . with its syntax being :match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
# day = 4
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday") # it prints the day no 4 from the above itterations 

# day = 4
# match day:
#   case 6:
#     print("Today is Saturday")
#   case 7:
#     print("Today is Sunday")
#   case _: ##case_ helps to avoid error by providing the missing value when their is no match
#     print("Looking forward to the Weekend")


## Cobine match 
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Today is a weekday")
#   case 6 | 7:
#     print("I love weekends!")

## if statement as a guard ( we can use if in match for an extra condition-check)

# month = 5
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month == 4:
#     print("A weekday in April")
#   case 1 | 2 | 3 | 4 | 5 if month == 5:
#     print("A weekday in May")
#   case _:
#       print("no match")