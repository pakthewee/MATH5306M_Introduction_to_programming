#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 15:12:39 2025

@author: paktheweerangthong

"""

""" Lecture Notes 1: [20251006] """

## data type
## str = string
## int = integer
## float = floating - point number

## control flow
## for loop

## operations
## + addition
## * mutiplication
## [str] + [str] is concatenation

## syntax
## () string delimeters
## ""
## = cariable assignment
## :
## f"
## {}
## """ """ block string

#%%

""" Part 1: Input syntax """
### Script 1:

first_input = input("Please input the first number: ")
second_input = input("Please input the second number: ")

first_number = int(first_input)
second_number = int(second_input)

product = first_number * second_number

if product > 50:  # control flow
    print("The product is greater than 50")
    print("Thank you")
else:
    print("The product is not greater than 50")
    print("Thank you")
    
#%%  
    
### Script 2:
    
first_input = input("Please input the first number: ")
second_input = input("Please input the second number: ")

first_number = int(first_input)
second_number = int(second_input)

product = first_number * second_number

if product > 50:
    result = "is"

else:
    result = "is not"
    
    print("The product " + result +" greater than 50")
    print("Thank you")

#%%

### Script 3:

first_input = input("Please input the first number: ")
second_input = input("Please input the second number: ")

first_number = int(first_input)
second_number = int(second_input)

product = first_number * second_number

if product > 50:
    result = "is"

else:
    result = "is not"
    
    print("The product " + result +" greater than 50")
    print("Thank you")
    print(f"The product of the first number is {first_input} and the second number is {second_number}")

#%%

""" Part 2: Calculating the math """

""" 
Task 1: Calculate the area of a right-angled triangle, 
taking the length pf the hypoteneuse and the size of the of one other angle as input
"""
# formula
# f1. Area = 1/2 * r^2 sin() cos() ## sin funtion use radians not angle
# f2. Area = 1/4 * r^2 * sin2() ## optimzing the f1

""" Calculate the area of a triangle from length of hypoteneuse and one angle """
length = input("Please input the length of the hypoteneuse (in cm): " )
angle = input("Please enter the angle (in degree): ")

import math
# area = float(length)**2 * math.sin(2*float(angle)) / 4
area = float(length)**2 * math.radians(2*float(angle)) / 4

# print(f"The area is {area} cm^2")
print(f"The area is {round(area, 3)} cm^2 to 3d.p")


#%%
"""
Task 2: Calculate the area of a triangle from length of hypoteneuse and one angle
"""

import math

length = float(input("Please input the length of the hypoteneuse (in cm): "))
angle = float(input("Please enter the angle (in degrees): "))

area = length**2 * math.sin(math.radians(2*angle)) / 4

print(f"The area is {round(area, 3)}cm^2 to 3d.p.")

#%%









