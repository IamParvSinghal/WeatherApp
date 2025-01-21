# # This is what I love
# # print("I love pizza")

# first_name = "Parv"
# last_name = "Singhal"
# # (first_name + " " + last_name) # + is used as concatenation
# # print(f"Hello {first_name}, hope you have a good day!") # this print sentence uses f string

# # Typecasting
# age = 19
# gpa = 3.76
# is_student = True

# # print(type(age)) # prints type of variable. Output - <class 'int'>
# # (int(gpa)) # converts gpa to an int. Output - 3
# # (bool(first_name)) # always returns True when bool is called on a string unless string is empty

# # input("Where do you study?: ") # allows user input. User input is stored as a string

# # Exercise 1: Calculate area of a rectangle
# # Get length and width from user
# def baller(peenar):
#     while True:
#         try:
#             value = float(input(peenar))
#             return value
#         except ValueError:
#             print("Don't skibidi sigma me lil bro")

# length = baller("Input Length: ")
# width = baller("Input Width: ")

# # Convert length and width to float from string since user input is stored as a string
# l_int = float(length)
# w_int = float(width)

# # area of rectangle
# area = l_int * w_int
# print(f"The area of the rectangle is: {area}")

# x = -6.782376432

# print(round(x, 3)) # prints -6.782
# print(abs(x)) # prints 6.782376432
# print(pow(x, 2)) # prints 46.00063006534906

# calculate circumference of a circle: 2*pi*r
import math
# radius = input("Radius: ")
# radius_int = float(radius)
# circumference = 2*math.pi*radius_int
# print(f"The circumference of circle with radius {radius} is: {circumference}")

# age = float(input("Age: "))
# if age >= 18:
#     print("Welcome!")
# elif age <= 0:
#     print("Lil Bro ahh")
# else:
#     print("Nuh uh")

# conditional operations: X if condition else Y
# x = 10
# print("Positive" if x > 0 else "Negative")

# string methods:
# name = "parv singhal"
# print(len(name)) # returns int. output = 12
# print(name.find("a")) # returns int index of FIRST occurence of " ". returns -1 if not found. output = 1
# print(name.rfind("a")) # returns int index of LAST occurence of " ". returns -1 if not found. output = 10
# print(name.capitalize()) # capitalizes first letter of string. output = Parv singhal
# print(name.upper()) # every letter in string in uppercase. output = PARV SINGHAL
# print(name.lower()) # every letter in string in lowercase. output = parv singhal
# print(name.isdigit()) # returns true if and only if the string contains integers only
# print(name.isalpha()) # returns true if and only if the string contains alphabets only (space not included)
# print(name.count("a")) # counts the total occurences. output = 2
# print(name.replace(" ", "_")) # replaces all occurences of first arguement with the second. 

# user = input("Enter username: ")
# if len(user) > 12 or not user.find(" ") == -1 or not user.isalpha():
#     print("Invalid input")
# else:
#     print("Valid input")

# indexing: [start:end:step]. only works with strings
# int = "1234567890"
# print(int[0:4]) # 1234
# print(int[:6]) # 123456
# print(int[3:]) # 4567890
# print(int[-1]) # 0
# print(int[::2]) # 13579
# print(int[-4:]) # 7890
# print(int[::-1]) # 0987654321

# price = 114.43212
# print(f"The price is {price:.2f}") # 114.43
# print(f"The price is {price:10}") #   114.43212
# print(f"The price is {price:010}") # 0114.43212
# print(f"The price is {price:.2f}") # 114.43

# lists [] - ordered and changable. Allows duplicates
# sets {} - unordered and immutable, meaning you cannot change existing values. However you can add and remove elements. No duplicates
# tuples () - ordered and unchangeable. cannot change elements and cannot add or remove elements. faster than lists because less memory usage
#                                                                                                 since tuples are unchangeable. Allows duplicates

# Dictionaries: ordered and changeable. No duplicates allowed. does not have to be strings. can be any object.
# price = {"Apple" : "$5",
#          "Banana" : "$3",
#          "Orange" : "$4",
#          "Mango" : "$8"}

# print(price.get("Orange")) # prints "$4". If not found then prints "None"
# price.update({"Pineapple" : "$5.50"}) #adds a new key with pineapple at a price of $5.50
# price.update({"Mango" : "$7"}) # changes price of mango from $8 to $7.
# price.pop("Apple") # removes the key "Apple"
# price.popitem() # removes the newest item

# # the fruit name is called the key and the price is called the values
# # you can access all the keys by using:
# keys = price.keys()
# #you can access all the values by using:
# values = price.values()

# print(price) # {'Banana': '$3', 'Orange': '$4', 'Mango': '$7'}
# print(keys) # dict_keys(['Banana', 'Orange', 'Mango'])
# print(values) # dict_values(['$3', '$4', '$7'])

