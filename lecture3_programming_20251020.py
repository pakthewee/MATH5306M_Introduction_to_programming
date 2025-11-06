#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 15:07:39 2025

@author: paktheweerangthong
"""

""" Lecture Notes 3: [20251020] """

# types: list -> for store the value in the list
# syntax: [ , ,] -> list delimeters
# defind betweeen entries: ,
# zero index: []
# newline character: \n
# while number division: // 
# remainder : % 
# function: def, return

#%%    

"""
Caluclate required coin values for change:
"""

### Script 1:
    
# Example from last week
remaining_value = int(input("Please input the required change in pence: "))

num_of_2P = 0
while remaining_value >= 200:
    num_of_2P += 1
    remaining_value -= 200
    print(f"remaining_value: {remaining_value}\n"
          f"num_of_2P: {num_of_2P} ")

else:
    print("remaining_value was less than 200 to Loop has exited")

num_of_1P = 0
while remaining_value >= 100:
    num_of_1P += 1
    remaining_value -= 100

num_of_50p = 0
while remaining_value >= 50:
    num_of_50p += 1
    remaining_value -= 50
    
num_of_20p = 0
while remaining_value >= 20:
    num_of_20p += 1
    remaining_value -= 20
    
num_of_10p = 0
while remaining_value >= 10:
    num_of_10p += 1
    remaining_value -= 10
    
num_of_5p = 0
while remaining_value >= 5:
    num_of_5p += 1
    remaining_value -= 5
    
num_of_2p = 0
while remaining_value >= 2:
    num_of_2p += 1
    remaining_value -= 2
    
num_of_1p = 0
while remaining_value >= 1:
    num_of_1p += 1
    remaining_value -= 1

print(f"Number of £2 coins: {num_of_2P}; remaining: {remaining_value}")
print(f"Number of £1 coins: {num_of_1P}; remaining: {remaining_value}")
print(f"Number of 50p coins: {num_of_50p}; remaining: {remaining_value}")
print(f"Number of 20p coins: {num_of_20p}; remaining: {remaining_value}")
print(f"Number of 10p coins: {num_of_10p}; remaining: {remaining_value}")
print(f"Number of 5p coins: {num_of_5p}; remaining: {remaining_value}")
print(f"Number of 2p coins: {num_of_2p}; remaining: {remaining_value}")
print(f"Number of 1p coins: {num_of_1p}; remaining: {remaining_value}")

#%%

"""from the console"""
# coin_value
# Out[39]: [200, 100, 50, 20, 10, 5, 2, 1]

# coin_value[0]
# Out[40]: 200

# coin_value[1]
# Out[41]: 100

# coin_value = [200, 100, 50, 20 ,10 ,5 ,2 ,1]

# for coin in coin_value:
#     print(coin)

# output    
# 200
# 100
# 50
# 20
# 10
# 5
# 2
# 1

#%%

remaining_value = change_value = int(input("Please input the required change in pence: "))

coin_value = [200, 100, 50, 20 ,10 ,5 ,2 ,1]

message = f"To make {change_value}, please dispense:\n"

for coin in coin_value:
    count = 0
    while remaining_value >= coin:
        count += 1 ## number of 200p coin that we count
        remaining_value -= coin ## calculate the remainning value after subtract the 200p coins
    message += f"{count} coins of value {coin}p\n" 
    
print(message)


# output
# Please input the required change in pence: 215
# To make 215, please dispense:
# 1 coins of value 200p
# 0 coins of value 100p
# 0 coins of value 50p
# 0 coins of value 20p
# 1 coins of value 10p
# 1 coins of value 5p
# 0 coins of value 2p
# 0 coins of value 1p


#%%

"""
Caluclate required coin values for change:
syntax

    738/200
    Out[46]: 3.69

    738//200
    Out[47]: 3

    738%200
    Out[49]: 138
    
"""

remaining_value = change_value = int(input("Please input the required change in pence: "))

coin_value = [200, 100, 50, 20 ,10 ,5 ,2 ,1]

message = f"To make {change_value}, please dispense:\n"

for coin in coin_value:
    count = remaining_value // coin
    remaining_value = remaining_value % coin
    message += f"{count} coins of value {coin}p\n" 
    
print(message)

#%%

"""
Task 9: Sum of the digits of a number
"""

number = int(input("Please input a whole number: "))

def nth_digit(number, n):
    """ Find the n-th please digit in number """
    the_digit = (number // (10**(n-1))) % 10
    return the_digit

#%%