#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 07:10:37 2025

@author: paktheweerangthong
"""

""" Lecture Notes 5: [20251103] """

# Syntax: 
# {} -> dictionary
# :  -> dictionary delimiters
#       e.g. {1: 'first', 2: 'second'}
# sum(<list>)

# In-built functions
# sorted(<list>)
# n from the end
# last index 1 from thread

# Methods
# <list>.sort()

#%%

""" Sum the digits of a number """

### Script 1:

number_string = input("Please input a whole number: ")

try:
    digits_list = []
    
    for i in number_string:
        digits_list.append(int(i))
        print(digits_list)
    print(f"The sum of the digits in {number_string} is {sum(digits_list)}")
except ValueError:
    print("You have not input a valid number: ")
    
    
# result:
# Please input a whole number: 56789
# [5]
# [5, 6]
# [5, 6, 7]
# [5, 6, 7, 8]
# [5, 6, 7, 8, 9]
# The sum of the digits in 56789 is 35
    
#%%

### Script 2:
    
number_string = input("Please input a whole number: ")

try:
    digit_list = [int(i) for i in number_string]
    print(digits_list)
    print(f"The sum of the digits in {number_string} is {sum(digits_list)}")
except ValueError:
    print("You have not input a valid number: ")
    
# result
# Please input a whole number: 56789
# [5, 6, 7, 8, 9]
# The sum of the digits in 56789 is 35
    
#%%

""" Task : Give the number of sides of a shape"""

### Script 1:

POLYGONS = {"triangle":3, "square":4, "pentagon":5, "hexagon":6}

name = input("Please enter the name of a shape: ")
print(f"A {name} has {POLYGONS[name]} sides")

# result
# Please enter the name of a shape: triangle
# A triangle has 3 sides

#%%

### Try on console

POLYGONS = {"triangle":3, "square":4, "pentagon":5, "hexagon":6, 572: False}

POLYGONS[572]
Out[37]: False

POLYGONS["square"]
Out[38]: 4

POLYGONS["triangle"]
Out[39]: 3

#%%

### Script 2:

POLYGONS = {"triangle":3, "square":4, "pentagon":5, "hexagon":6, 572: False}

name = input("Please enter the name of a shape: ")
print(f"A {name} has {POLYGONS[name.lower()]} sides")

# result
# Please enter the name of a shape: Square
# A Square has 4 sides

#%%

### Script 3:

POLYGONS = {"triangle":3, "square":4, "pentagon":5, "hexagon":6, 572: False}

name = input("Please enter the name of a shape: ")

try:
    print(f"A {name} has {POLYGONS[name.lower()]} sides")
except KeyError:
    print(f"The shape '{name}' is not defined in this program")

# result
# Please enter the name of a shape: Circle
# The shape 'Circle' is not defined in this program

#%%

""" Task : Remove the outliers """

### Script 1

def remove_outliers(value_list, n):
    """ Remove n Largest and smallest values from value_list """
    value_list.sort()
    return value_list[n:-n]

digits_list = [3, 2, 9, 8, 3, 2]
chk = remove_outliers(chk_list, 1)
print(chk)

# result
# [2, 3, 3, 8]

#%%

### Try on console
digits_list = [3, 2, 9, 8, 3, 2]

digits_list[-3]
Out[49]: 8

digits_list[-4]
Out[51]: 9

digits_list[2:5]
Out[52]: [9, 8, 3]

digits_list[2:-1]
Out[53]: [9, 8, 3]

digits_list[2:-2]
Out[54]: [9, 8]

digits_list[9]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[50], line 1
----> 1 digits_list[9]

IndexError: list index out of range

#%%

""" Random Number"""

### Try on console

import random

random.randint(-100,100)
Out[57]: -7

random.randint(-100,100)
Out[58]: 69

random.randint(-100,100)
Out[59]: -21

random.randint(-100,100)
Out[60]: 78

#%%

### Script 2

def remove_outliers(value_list, n):
    """ Remove n Largest and smallest values from value_list """
    value_list = sorted(value_list) # change from value_list.sort() to value_list.scorted(value_list)
    return value_list[n:-n]

digits_list = [3, 2, 9, 8, 3, 2]
chk = remove_outliers(chk_list, 1)
print(chk)

# result
mylist = [random.randint(-100,100) for _ in range(20)]

#%%

### Try console

mylist = [random.randint(-100,100) for _ in range(20)]

print(mylist)
[39, 100, -91, 12, -4, 46, -95, -1, -44, -60, 93, 81, -63, -5, -2, -61, -4, 90, -60, -21]

my_number = 3

print(remove_outliers(mylist, my_number))
[-61, -60, -60, -44, -21, -5, -4, -4, -2, -1, 12, 39, 46, 81]

#%%


### Try console
[i for i in range(1, n+1) if n % i == 0]
Out[77]: [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72]

