import math

#                       Python Crib sheet


# Input function
    # logs user input
# print(input('who are you crunchy?'))
#


#               # String manipulation


#     # multiple line text using ''' ''''
# text: str = ''' Online application for the visit to Japan with tourism purpose (single-entry)】
#             All foreign nationals/people who need to obtain a short-term visa to Japan AND currently
#             '''
# print(text)

# String indexing

# name: str = 'Ivan the terrible!'
# print(name[0]) # returns first character
# print(name[-1]) # returns last character
# print(name[1:-1]) # returns all characters between first and last
# print(name[0:4]) # returns first to fourth character
# print(name[0:]) # returns first to remainder
# print(name[:4]) # returns up to fourth character
# print(name[:]) # returns all

# Formated strings
    # inserting strings in other strings by using f''
# thing: str = 'goooooooold'
# print(f'hey there sunny. now where did all the {thing} go?')

# String methods
    #inbuilt methods for strings
# greetings: str = 'hello world'

# print(len(greetings), 'characters long') # returns character length
# print(greetings.upper())
# print(greetings.lower())
# print(greetings.title())
# print(greetings.find('h')) # return index number
# print(greetings.replace('hello','goodbye'))
# print('df' in greetings) # search function, return bool value

            # Math

# math operators
# print(6 + 5)
# print(6 - 5)
# print(6 * 5)
# print(6 / 5) # division with float result
# print(6 // 5) # division with int result
# print(6 % 5) # division with remainder
# print(6 ** 5) # exponents, 5 to the power of 6

# math functions
    # all math functions can be imported with a statement
    # using math.method

# x: float = 2.9
# print(round(x)) # round
# print(abs(-x)) # absolute value
# print(math.ceil(x))
#
# # if/else
#
# house_price: int = 1_000_000_000
# good_credit: bool = True
# down_payment: float = 0.1 * house_price
#
# if good_credit:
#     print(f'you can place your down payment of £{round(down_payment)}')
# else:
#     print('sorry babay')

# Logical operators
    # and both options has to be true
    # or one of the option has to be true
    # not: the opposite of the current boolean state


# comparison operators
    # >
    # <
    # <=
    # >=
    # ==
    # !=

# while loops
    # as long condition is true the loop runs
# i: int = 1
#
# while i <= 5:
#     print(i * '@')
#     i = i + 1

# for loops
    # good for iterating over items or strings
#
# for i in ['jimmy', 'jango', 'alfa','zulu']: # loop a list
#     print(i)
#
# for i in (1,2,3,4,5,'jim'):  # loop a tuple
#     print(i)
#
# for i in {'key':'door'}:  # loop a dictionary
#     print(i)
#
# for i in ['jimmy', 'django', 'alfa', 'zulu']:  # loop a list
#     print(i)
# for i in range(10):  # loop a number range
#     print(i)

# Nested loops
    # A nested loop in Python refers to a loop within another loop.
    # The “inner loop” will be executed one time for each iteration of
    # the “outer loop”. This structure is commonly used when you need
    # to perform operations on multi-dimensional data structures like
    # lists of lists, or when processing tasks that require multiple
    # levels of looping.

# Demo nested loop
# for i in range(1, 4):  # Outer loop
#     for j in range(1, 4):  # Inner loop
#         print(f'i = {i}, j = {j}')

# multiplication table nested loop

# # running outer loop from 2 to 3
# for i in range(2, 3):
#     # printing inside outer loop
# # running inner loop from 1 to 10:
#     for j in range(1, 13):
#         # printing inside inner loop
#         print(i, '*', j, '=', i * j)
#
        # NESTED LOOPS PATTERNS
#     # square pattern
# x: int = 5
#
# for r in range(x): # outer loop controls rows
#     for c in range(x):  # inner loop controls columns
#         print('*', end=' ')
#     print()

#    # increasing left side triangle pattern

# x: int = 6
# # creates row, 6 in this case
# for r in range(x): # outer loop controls rows
#
#     # with every new row, add 1 star
#     for c in range(r + 1):  # inner loop controls columns
#         print('*', end=' ')
#     print()
#
# #    # decreasing left side triangle pattern
#
# x: int = 6
# # creates row, 6 in this case
# for r in range(x): # outer loop controls rows
#
#     # with every new row, add 1 star
#     for c in range(r, x):  # inner loop controls columns
#         print('*', end=' ')
#     print()

#       # right side triangle

stars: int = 6

for r in range(stars):

    for c in range(r,stars):
        print(' ', end='')

    for c in range(r + 1):
        print('*', end='')
    print()





























# Error handling











# # Data types
#
# numbers: int = 10 # any number
# decimal: float = 1.0 # any decimal number
# txt: str = 'anything here' # anything between quotations
# active: bool = False  # 2 states: true or false
#
# names: list = ['swiper','table'] # mutable list
# coordinates: tuple = (1.5, 2.5) # immutable list
# unique: set = {1,2,3,89} # unique set of anything, no repeats
# data: dict = {'name':'heman', 'age':'2000'} # key and value pairs
#
#
# # Type annotation:
#     # a way to allow code be more humanreadable
#
# name: str = 'i am text' # greate way to catch type errors
#
# # Constants
#     # immutable data types in any other language but not here
#
# PI: Final[float] = 3.1415
#     # an extension will be imported for the Final keyword
#     # from typing_extensions import Final
#
#     # PI is the annotation part
#     # Final[] allows the declaration of data type
#     # 3.14 is data type
#     # data still mutable but will notify upon attempting such
#
# # Functions
#     # a code containers that executes some functionality
# print('current time is: ', datetime.now())
#     # inbuilt function datetime.now()
#
#     # creating reusable functions:
# def show_datetime() -> None :
#     print('current time is: ', datetime.now())
#
#     # function call
#     show_datetime()
#
#     # create functions that takes some parameters
#     def greet(name: str) -> None: # -> None, means it does not return anything for the reader
#         print(f'hello,{name}')
#     # function call
#     greet('jimmy')
#
#     # create function that takes parameters and returns results
#     def add(a: float, b: float) -> float:
#         return a + b
#     # function call
#     print(add(89,8979897))
#
# # Classes
#     # a house for objects and functions to live ever after
# class Car: # the house
#     # the guy that manages the house named constructor
#     def __init__ (self, brand: str, speed: int) -> None:
#         self.brand = brand
#         self.speed = speed
#
# # Methods
#     # functions nested in classes called methods
#     def top_speed(self) -> None:
#         print(f'its top speed is {self.speed}')
#
#
#     def car_type(self) -> None:
#         print(f'a great brand named {self.brand}')
#
#
#     # class object instance creation
# nissan: Car = Car('BMW GTR-35',270)
#
#     # class method call
# print(nissan.top_speed(), nissan.car_type())
#
#     # class object call without method
# print(nissan.brand, nissan.speed)
#
#
# # Dunder methods
#     # double underscore methods __init__
#     # methods are inbuilt and call them sells automatically once
#     # object is created, they perform many operations
#
#
# class Fruits:
#     def __init__(self, name: str) -> None:
#         self.name = name
#
#     # takes a number and returns answer as string
#     def __mul__(self, other: int) -> str:
#         return self.name * other
#
#     #create object
# mango: Fruits = Fruits('is not mango ')
#
#     # call it
# print(mango * 8)


















        # Really nice practices

# if __name__ == "__manin__" Method

# just type main and press tab
# it tells the interpreter to run function only if its runs
# directly where the function lives but not if imported, basically
# allowing to run any function only once if called.

# def connect()-> None:
#     print('connecting....')
#     time.sleep(2)
#     print('connected')
#
# if __name__ == "__main__":
#     connect()
# # this code will only run once at any given time


# List comprehension
    # using list function to loop through list

# function that loops through a list


# def find_them()-> None:
#     things: list[str] = ['mango', 'champaign',
#                        'the man who sold the world']
#     long_names: list[str] = []
#     for i in things:
#         if len(i) > 5:
#             long_names.append(i)
#     print(long_names)
#
# if __name__ == '__main__':
#     find_them()
#
#     # Now using list comprehension
#     # without using append(), an extraction took place
#     things: list[str] = ['mango', 'champaign',
#                             'the man who sold the world']
#     long_names: list[str] = [i for i in things if len(i) > 5]
#     print(long_names)