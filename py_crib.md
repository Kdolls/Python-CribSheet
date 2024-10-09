# py_crib

## data structures and methods:

### Lists

#### Indexing/Slicing Methods

```
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

print(my_list[:2])  # Output: [1, 2]
print(my_list[2:])  # Output: [3, 4, 5]
print(my_list[1:3])  # Output: [2, 3]
```

#### Methods

```
my_list = [1, 2, 3]

# append()
my_list.append(4)
print(my_list)   # Output: [1, 2, 3, 4]

# extend()
my_list.extend([4, 5])
print(my_list)   # Output: [1, 2, 3, 4, 5]

# insert()
my_list.insert(1, 4)
print(my_list)   # Output: [1, 4, 2, 3]
```

### Tuples

#### Indexing/Slicing Methods

```
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5

print(my_tuple[:2])  # Output: (1, 2)
print(my_tuple[2:])  # Output: (3, 4, 5)
print(my_tuple[1:3])  # Output: (2, 3)
```

#### Methods

*Note: Tuples are immutable, so there are no methods to modify them.*

### Dictionaries

#### Indexing/Slicing Methods

```
my_dict = {'a': 1, 'b': 2}
print(my_dict['a'])  # Output: 1

# get all keys
print(list(my_dict.keys()))  # Output: ['a', 'b']
```

#### Methods

```
my_dict = {'a': 1, 'b': 2}

# update()
my_dict.update({'c': 3, 'd': 4})
print(my_dict)   # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# pop()
print(my_dict.pop('a'))  # Output: 1
print(my_dict)   # Output: {'b': 2}
```

### Sets

#### Methods

```
my_set = {1, 2, 3}

# add()
my_set.add(4)
print(my_set)   # Output: {1, 2, 3, 4}

# remove()
my_set.remove(2)
print(my_set)   # Output: {1, 3}
```

### Stacks

#### Methods

*Note: Python does not have built-in support for stacks as a data structure. The above methods 
are implemented using lists.*

```
my_stack = [1, 2, 3]

# push()
my_stack.append(4)
print(my_stack)   # Output: [1, 2, 3, 4]

# pop()
print(my_stack.pop())  # Output: 3
print(my_stack)   # Output: [1, 2]
```

### Queues

#### Methodsd

ffo*Note: Python does not have built-in support for queues as a data structure. The above methods 
are implemented using lists.*

```
my_queue = [1, 2, 3]

# enqueue()
my_queue.append(4)
print(my_queue)   # Output: [1, 2, 3, 4]

# dequeue()
print(my_queue.pop(0))  # Output: 1
print(my_queue)   # Output: [2, 3]
```

### Deques

#### Methods

*Note: Python does not have built-in support for deques as a data structure. The above methods 
are implemented using lists.*

```
my_deque = [1, 2, 3]

# append()
my_deque.append(4)
print(my_deque)   # Output: [1, 2, 3, 4]

# pop()
print(my_deque.pop())  # Output: 3
print(my_deque)   # Output: [1, 2]
```

### Graphs

#### Methods

*Note: Python does not have built-in support for graphs as a data structure. The above methods 
are implemented using dictionaries and lists.*

```
my_graph = {'A': ['B', 'C'], 'B': ['D'], 'C': []}

# add_edge()
my_graph['A'].append('E')
print(my_graph)   # Output: {'A': ['B', 'C', 'E'], 'B': ['D'], 'C': []}

# remove_edge()
my_graph['A'].remove('C')
print(my_graph)   # Output: {'A': ['B', 'E'], 'B': ['D'], 'C': []}
```

### Trees

#### Methods

*Note: Python does not have built-in support for trees as a data structure. The above methods 
are implemented using dictionaries and lists.*

```
my_tree = {'A': {'B': 1, 'C': 2}, 'B': {}, 'C': {}}

# add_child()
my_tree['A']['D'] = 3
print(my_tree)   # Output: {'A': {'B': 1, 'C': 2, 'D': 3}, 'B': {}, 'C': {}}

# remove_child()
del my_tree['A']['B']
print(my_tree)   # Output: {'A': {'C': 2, 'D': 3}, 'B': {}, 'C': {}}
```

**1. `append()`**: Adds an element to the end of the list.

Example:

```
my_list = ['a', 'b']
my_list.append('c')
print(my_list)  # Output: ['a', 'b', 'c']
```

**2. `insert(index, value)`**: Inserts a new element at the specified 
position.

Example:

```
my_list = ['a', 'b']
my_list.insert(0, 'c')
print(my_list)  # Output: ['c', 'a', 'b']
```

**3. `extend(iterable)`**: Adds multiple elements to the end of the list.

Example:

```
my_list = ['a', 'b']
my_list.extend(['c', 'd', 'e'])
print(my_list)  # Output: ['a', 'b', 'c', 'd', 'e']
```

**4. `remove(value)`**: Removes the first occurrence of a value in the 
list.

Example:

```
my_list = ['a', 'b', 'c']
my_list.remove('b')
print(my_list)  # Output: ['a', 'c']
```

**5. `pop(index=-1)`**: Removes the element at the specified position and 
returns it.

Example:

```
my_list = ['a', 'b', 'c']
popped_element = my_list.pop(0)
print(popped_element)  # Output: 'a'
print(my_list)  # Output: ['b', 'c']
```

**6. `index(value)`**: Returns the index of the first occurrence of a 
value in the list.

Example:

```
my_list = ['a', 'b', 'c']
index = my_list.index('b')
print(index)  # Output: 1
```

**7. `count(value)`**: Returns the number of occurrences of a value in the
list.

Example:

```
my_list = ['a', 'a', 'b', 'c']
count = my_list.count('a')
print(count)  # Output: 2
```

**8. `sort()`**: Sorts the elements of the list in ascending order.

Example:

```
my_list = [4, 2, 1, 3]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]
```

**9. `reverse()`**: Reverses the order of the elements in the list.

Example:

```
my_list = ['a', 'b', 'c']
my_list.reverse()
print(my_list)  # Output: ['c', 'b', 'a']
```

**Really Nice Practices**
================================

If `__name__` == ` "__main__"`, Method
-----------------------------------

Just type `main` and press Tab. It tells the interpreter to run a function
only if it's run directly where the function lives, but not if imported. 
This allows you to run any function only once if called.

```
def connect()-> None:
    print('connecting....')
    time.sleep(2)
    print('connected')
```

If `__name__` == ` "__main__"`: `connect()`

This code will only run once at any given time.

**List Comprehension**
=====================

Using list comprehension to loop through a list:

```
def find_them()-> None:
    things: list[str] = ['mango', 'champaign',
                         'the man who sold the world']
    long_names: list[str] = []
    for i in things:
        if len(i) > 5:
            long_names.append(i)
    print(long_names)

if __name__ == '__main__':
    find_them()
```

Now using list comprehension (without using `append()`, an extraction took
place):

```
things: list[str] = ['mango', 'champaign',
                         'the man who sold the world']
long_names: list[str] = [i for i in things if len(i) > 5]
print(long_names)
```

**Class Stack**
=============

```
class Stack:
    def __init__(self):
        self.elements = ['12', 'mahmoud', 'ducks', '@*&)^%(*', 'randomly 
ya 7abeby']

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        else:
            return None

    def is_empty(self):
        return len(self.elements) == 0
```

If `__name__` == ` '__main__'`:

```
someList: list = ['12', 'mahmoud', 'ducks', '@*&)^%(*', 'randomly ya 
7abeby']
x = Stack()
print(x.elements)
```

### Python `for` Loops

A `for` loop is used to iterate over a sequence (such as a list, tuple, or
string) or other iterable objects.

#### Example 1: Iterating over a List

```python
# Define a list of fruits
fruits = ['apple', 'banana', 'cherry']

# Use a for loop to print out each fruit
for fruit in fruits:
    print(fruit)
```

Output:

* apple
* banana
* cherry

#### Example 2: Iterating over a Dictionary

```python
# Define a dictionary of student names and ages
students = {'John': 25, 'Jane': 30, 'Bob': 20}

# Use a for loop to print out each student's name and age
for name, age in students.items():
    print(f"{name} is {age} years old.")
```

Output:

* John is 25 years old.
* Jane is 30 years old.
* Bob is 20 years old.

#### Example 3: Iterating over a Range

```python
# Use a for loop to print out the numbers from 1 to 5
for i in range(1, 6):
    print(i)
```

Output:

* 1
* 2
* 3
* 4
* 5

#### Example 4: Using `enumerate` to iterate over a list with index

```python
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use a for loop to print out each number along with its index
for i, num in enumerate(numbers):
    print(f"Index {i}: {num}")
```

Output:

* Index 0: 1
* Index 1: 2
* Index 2: 3
* Index 3: 4
* Index 4: 5

These examples demonstrate the basic syntax and usage of Python `for` 
loops.

... 
**Python Function**
=====================

A Python function is a block of code that can be executed multiple times 
from different parts of your program. It's defined using the `def` keyword
followed by the name of the function and parentheses containing its 
parameters.

Example:

```python
def greet(name):
    print(f"Hello, {name}!")
```

You can then call this function with a specific argument, like so:

```python
greet("John")
```

This would output: `Hello, John!`

**Scope**
==========

In Python, scope refers to the region of code where a variable is defined 
and accessible. A variable's scope determines its visibility and 
accessibility.

There are two types of scopes in Python:

1. **Local Scope**: Variables defined inside a function have local scope. 
   They can only be accessed within that function.
2. **Global Scope**: Variables defined outside any function (i.e., at the 
   top-level) have global scope. They can be accessed from anywhere in your 
   program.

Example:

```python
x = 10  # global variable

def test():
    x = 20  # local variable with the same name as the global one
    print(x)

print(x)
test()
print(x)
```

Output:

```
10
20
10
```

As you can see, the `x` inside the function has a different value than the
global `x`, because they have separate scopes.

**List Comprehensions**
=====================

A list comprehension is a concise way to create a new list from an 
existing iterable. It's defined using square brackets `[]` and contains a 
single expression that's evaluated for each element in the iterable.

Example:

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)
```

Output: `[1, 4, 9, 16, 25]`

This code creates a new list `squared_numbers` containing the squares of 
each number in the original list `numbers`.

**Example with Multiple Conditions**
-----------------------------------

You can also use list comprehensions with multiple conditions using `if` 
statements.

Example:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
```

Output: `[2, 4]`

This code creates a new list `even_numbers` containing only the even 
numbers from the original list.

Python Lambda Functions
=====================

A lambda function (also known as an anonymous function) is a small, 
single-expression function that can be defined inline within a Python 
program.

### Syntax

Lambda functions follow the following syntax:

```
lambda arguments : expression
```

Where:

- `arguments` is a comma-separated list of variables.
- `expression` is the code to be executed when the lambda function is 
  called.

### Example

Here's an example that calculates the square of a number:

```
square = lambda x: x ** 2
print(square(4))  # Output: 16
```

In this example, we define a lambda function `square` that takes one 
argument `x`. The function returns the square of `x`.

### Using Lambda Functions

Lambda functions are often used as:

- Higher-order functions (functions that take other functions as 
  arguments).
- Map, filter, and reduce operations.
- Event handlers.

Here's an example of using a lambda function with the `map` function:

```
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

In this example, we use the `map` function to apply the lambda function to
each element in the `numbers` list.

### Advantages of Lambda Functions

Lambda functions offer several advantages:

- Concise syntax.
- Easy to define small, one-off functions.
- Can be used as higher-order functions.

However, they also have some limitations. For example:

- They can't be reused or called multiple times.
- They can't contain complex logic or statements.

### When to Use Lambda Functions

Use lambda functions when:

- You need a simple, one-off function.
- You want to define a small, concise function.
- You're working with functional programming concepts (like `map`, 
  `filter`, and `reduce`).

Python has a vast array of modules that can be used to perform various 
tasks. Here are some of the most commonly used modules, along with 
examples:

### **math**

================
The `math` module contains mathematical functions like sin, cos, tan, etc.

Example:

```python
import math

print(math.pi)  # Output: 3.14159265359...
```

### **random**

================
The `random` module provides functionality for generating random numbers 
and performing random operations.

Example:

```python
import random

print(random.randint(1, 10))  # Output: a random integer between 1 and 10
```

### **time**

================
The `time` module provides various time-related functions like current 
time, sleep, etc.

Example:

```python
import time

print(time.time())  # Output: the current timestamp
```

### **re** (Regular Expressions)

=============================

The `re` module provides support for regular expressions in Python. 
Regular expressions are a powerful tool for working with text and pattern 
matching.

Example:

```python
import re

pattern = r"hello"
text = "hello world"

match = re.search(pattern, text)

if match:
    print("Found the pattern!")
```

### **csv** (Comma Separated Values)

=============================

The `csv` module provides functionality for reading and writing 
comma-separated values.

Example:

```python
import csv

with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Name', 'Age'])  # Write the header row
    writer.writerow(['John', 25])  # Write a data row
```

### **json** (JavaScript Object Notation)

=============================

The `json` module provides functionality for working with JSON data in 
Python. JSON is a lightweight format for exchanging data between systems.

Example:

```python
import json

data = {'name': 'John', 'age': 25}

print(json.dumps(data))  # Output: the JSON representation of the data
```

### **datetime**

================

The `datetime` module provides functionality for working with dates and 
times in Python. This is useful for tasks like formatting dates, 
calculating time differences, etc.

Example:

```python
import datetime

now = datetime.datetime.now()
print(now)  # Output: the current date and time
```

Python Files
=====================

In Python, a file is a collection of related code and data that can be 
saved on disk and re-used. Here are some examples of different types of 
Python files:

### **Hello World File**

```python
# hello.py

print("Hello, World!")
```

This is the simplest type of Python file: it just prints out "Hello, 
World!" to the console.

### **Math Operations File**

```python
# math_ops.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

result = add(5, 3)
print(result)  # Output: 8

result = subtract(10, 2)
print(result)  # Output: 8
```

This file defines two simple math operations (addition and subtraction) 
and demonstrates how to use them.

### **Data Structures File**

```python
# data_structures.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("John", 25), Person("Jane", 30)]

for person in people:
    print(f"{person.name} is {person.age} years old")
```

This file demonstrates how to define and use Python's built-in data 
structures, such as lists and classes.

### **Module File**

```python
# my_module.py

def greet(name):
    print(f"Hello, {name}!")

def goodbye(name):
    print(f"Goodbye, {name}!")

if __name__ == "__main__":
    greet("John")
    goodbye("Jane")
```

This file defines two simple functions (greet and goodbye) that can be 
used to interact with users. The `if __name__ == "__main__":` block allows
the file to be run directly from the command line.

### **Script File**

```python
# script.py

import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

print(calculate_area(5))  # Output: the area of a circle with radius 5
```

### Classes and Objects

In Python, a class is a blueprint for creating objects. An object is an 
instance of a class, and it has its own set of attributes (data) and 
methods (functions).

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

my_dog = Dog("Fido")
print(my_dog.name)  # prints "Fido"
my_dog.bark()  # prints "Woof!"
```

### Inheritance

Inheritance is the process by which one class can inherit the attributes 
and methods of another class. This allows for code reuse and facilitates 
the creation of a hierarchy of classes.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("The dog barks.")

my_dog = Dog("Fido")
print(my_dog.name)  # prints "Fido"
my_dog.sound()  # prints "The dog barks."
```

### Exceptions

Exceptions are a way to handle errors in Python. When an error occurs, an 
exception is raised, and it can be caught by a `try`/`except` block.

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    except TypeError:
        print("Both inputs must be numbers.")
    else:
        print(f"The result is {result}.")

divide(4, 2)  # prints "The result is 2.0."
divide(4, 0)  # prints "You cannot divide by zero!" 
```



## end...
