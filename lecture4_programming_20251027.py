#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 15:05:35 2025

@author: paktheweerangthong
"""

""" Lecture Notes 4: [20251027] """
    
# Keywords: elif, try
# Syntax: \
# Data types: list, str
# Built-in functions: len()

# Programming Quote:
# 1. "Look before you leap (LBYL)"
#    meaning:   -> Check everything before acting
#               -> Check conditions before performing an operation that might fail or cause an error
#    good for:  -> Critical systems (banking, finance, medical)
#               -> When an error could cause data loss or crash
#               -> When you can afford the extra check

# 2. "Easier to ask forgiveness than permission (EAFP)"
#    meaning:   -> Try first and handle the error if it happens
#    good for   -> Everyday scripting
#               -> Reading/writing files, API calls, or dynamic structures
#               -> Code that should stay readable and flexible

#%%

""" Part 1: Sum the digits of a number"""

### Script 1:
    
# number  = int(input("Please input a whole number: "))

def nth_digit(number, n):
    """Find the n-th place digit in number"""
    return (number // 10**(n-1)) % 10

chk = nth_digit(456,2)
print(chk)

### result
### nth_digit(456,1) -> return 6 
### nth_digit(456,2) -> return 5 
### nth_digit(456,3) -> return 4 

#%%

### Script 2:
    
def sum_of_digits(number):
    last_digit = number % 10
    rest = number // 10
    print(f"Last digit of {number} is {last_digit}; \n"
          f"Rest of {number} is {rest}.")
    
chk = sum_of_digits(456)
print(chk)

### result
### sum_of_digits(456)
### Last digit of 456 is 6; 
# Rest of 456 is 45.
# return -> None # no return value in the function
    
#%%

### Script 3:
    
def sum_of_digits(number):
    last_digit = number % 10
    rest = number // 10
    if rest == 0:
        return last_digit # e.g. 456 -> return 6
    else:
        return sum_of_digits(rest) + last_digit # e.g. 456 -> {rest} sum(4,5) + {last_digit} 6 = 15
chk = sum_of_digits(456)
print(chk)

### result
### sum_of_digits(456) -> return 15
    
    
#%%

### Script 4:

def sum_of_digits(number):
    """Find thesum of digits of number"""
    print(f"We are in sum_of_digits({number})")
    last_digit = number % 10
    rest = number // 10
    if rest == 0:
        print(f"In sum_of_digits({number}), we are returning {last_digit}")
        return last_digit
    else:
        print(f"In sum_of_digits({number}), we are calculating "
              f"sum_of_digits({rest}) + {last_digit}")
        result = sum_of_digits(rest) + last_digit
        print(f"In sum_of_digits({number}), we are returning {result}")
        return result
    
chk = sum_of_digits(456)
print(chk)

### result
# We are in sum_of_digits(456)
# In sum_of_digits(456), we are calculating sum_of_digits(45) + 6
# We are in sum_of_digits(45)
# In sum_of_digits(45), we are calculating sum_of_digits(4) + 5
# We are in sum_of_digits(4)
# In sum_of_digits(4), we are returning 4
# In sum_of_digits(45), we are returning 9
# In sum_of_digits(456), we are returning 15
# return -> 15


#%% 
## get the code from the screen

""" Part 2: Play with character"""

""" 
Task 11: Vowel or Consonant
Say whether a Letter is a vowel or a consonant
"""

### Script 1: 
    
letter = input("Please input a Letter: ")

if letter == "y":
    print(f"The Letter {letter} is sometimes a vowel and sometimes a consonant")
elif letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u': # use <or> condition for the vowel letters
    print(f"The letter {letter} is a vowel")
else:
    print(f"The letter {letter} is a consonant")

### result
# letter = 't' -> The letter t is a consonant
# letter = 'a' -> The letter a is a vowel
# letter = 'y' -> The letter y is a The Letter y is sometimes a vowel and sometimes a consonant

#%%

### Script 2:
    
letter = input("Please input a Letter: ")

if letter == "y":
    print(f"The Letter {letter} is sometimes a vowel and sometimes a consonant")
elif letter in ['a', 'e', 'i', 'o', 'u']: # create a list for the vowel letters
    print(f"The letter {letter} is a vowel")
else:
    print(f"The letter {letter} is a consonant")

### result
# letter = 't' -> The letter t is a consonant
# letter = 'a' -> The letter a is a vowel
# letter = 'y' -> The letter y is a The Letter y is sometimes a vowel and sometimes a consonant

#%%

### Script 3:
    
letter = input("Please input a Letter: ")

if letter == "y":
    print(f"The Letter {letter} is sometimes a vowel and sometimes a consonant")
elif letter in ['a', 'e', 'i', 'o', 'u']: # create a list for the vowel letters
    print(f"The letter {letter} is a vowel")
else:
    print(f"The letter {letter} is a consonant")
    
### result
# letter = 't' -> The letter t is a consonant
# letter = 'a' -> The letter a is a vowel
# letter = 'y' -> The letter y is a The Letter y is sometimes a vowel and sometimes a consonant
    
#%%

### Script 4:
    
letter = input("Please input a Letter: ")

if letter == "y":
    print(f"The Letter {letter} is sometimes a vowel and sometimes a consonant") 
elif letter in 'aeiou': # string is a list type, e.g. [a,b,c,d] = 'abcd' 
    print(f"The letter {letter} is a vowel")
else:
    print(f"The letter {letter} is a consonant")
    
### result
# letter = 't' -> The letter t is a consonant
# letter = 'a' -> The letter a is a vowel
# letter = 'y' -> The letter y is a The Letter y is sometimes a vowel and sometimes a consonant
    
#%% 

### Script 5:
    
letter = input("Please input a Letter: ")

if letter in "abcdefghijklmnopqrstuvwxyz":
    if letter == 'y':
        print(f"The Letter {letter} is sometimes a vowel and sometimes a consonant") 
    elif letter in 'aeiou': # string is a list type, e.g. [a,b,c,d] = 'abcd' 
        print(f"The letter {letter} is a vowel")
    else:
        print(f"The letter {letter} is a consonant")
else:
    print(f"{letter} is not a Letter of the alphabet")
    
### result
# letter = 't' -> The letter t is a consonant
# letter = 'a' -> The letter a is a vowel
# letter = 'y' -> The letter y is a The Letter y is sometimes a vowel and sometimes a consonant
# letter = 'A' -> A is a Capital Letter, so this is a sensitive character case -> ruturn "A is not a Letter of the alphabet"
# letter = 7 -> 7 is a number, so this is a sensitive character case -> ruturn "7 is not a Letter of the alphabet"

#%%

### Script 6

letter = input("Please input a Letter: ")

lower_letter = letter.lower()

if lower_letter in "abcdefghijklmnopqrstuvwxyz":
    if lower_letter == 'y':
        print(f"The Letter {letter} is sometimes a vowel and sometimes a consonant") 
    elif lower_letter in 'aeiou': # string is a list type, e.g. [a,b,c,d] = 'abcd' 
        print(f"The letter {letter} is a vowel")
    else:
        print(f"The letter {letter} is a consonant")
else:
    print(f"{letter} is not a Letter of the alphabet")
    
### result
# letter = 't' -> The letter t is a consonant
# letter = 'a' -> The letter a is a vowel
# letter = 'y' -> The letter y is a The Letter y is sometimes a vowel and sometimes a consonant
# letter = 'A' -> ruturn "The letter A is a vowel"
#               1. Accepts a letter (can be uppercase or lowercase),
#               2. Converts it to lowercase (so you can process it easily),
#               3. Checks if it’s a vowel,
#               4. Returns a sentence like → "The letter A is a vowel"
# letter = 7 -> 7 is a number, so this is a sensitive character case -> ruturn "7 is not a Letter of the alphabetbet"
# letter = 'cvb' -> 'cvb' ruturn " cvb is not a Letter of the alphabet"

#%%

### Script 7

letter = input("Please input a Letter: ")

lower_letter = letter.lower()

if lower_letter in "abcdefghijklmnopqrstuvwxyz" and len(letter) == 1: # check the letter length e.g. len('sexy') is 4, for this case we need only 1 character for the input
    if lower_letter == 'y':
        print(f"The Letter {letter} is sometimes a vowel and sometimes a consonant") 
    elif lower_letter in 'aeiou': # string is a list type, e.g. [a,b,c,d] = 'abcd' 
        print(f"The letter {letter} is a vowel")
    else:
        print(f"The letter {letter} is a consonant")
else:
    print(f"{letter} is not a Letter of the alphabet")
    
### result
# letter = t -> The letter t is a consonant
# letter = a -> The letter a is a vowel
# letter = y -> The letter y is a The Letter y is sometimes a vowel and sometimes a consonant
# letter = A -> ruturn "The letter A is a vowel"
#               1. Accepts a letter (can be uppercase or lowercase),
#               2. Converts it to lowercase (so you can process it easily),
#               3. Checks if it’s a vowel,
#               4. Returns a sentence like → "The letter A is a vowel"
# letter = 7 -> 7 is a number, so this is a sensitive character case -> ruturn "7 is not a Letter of the alphabet"
# letter = 'cvb' -> 'cvb' ruturn " cvb is not a Letter of the alphabet"

#%%

"""Part 3: Sum the digits of a number"""

number = input("Please input a whole number: ")

try:
    total = 0
    for i in number:
        total += int(i)
    print(f"The sum of the digits in {number} is {total}")
except ValueError:
    print("You have not input a valid number")

### result
# number = 7    -> The sum of the digits in 7 is 7
# number = 456  -> The sum of the digits in 456 is 15
# number = f    -> You have not input a valid number

#%%


