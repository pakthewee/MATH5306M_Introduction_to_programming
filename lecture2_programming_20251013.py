#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:19:23 2025

@author: paktheweerangthong
"""



""" Lecture Notes 2: [20251013] """

# Elements of style
# -- Modularity
# -- Readability

# In - built functions
# range(n) - successive whole numbers form 0 to n
# range(start, n)

#%%
""" 
Task 1: Sum the sequence numbers 

# Write a programme that reads a positive integer, n, 
# from the user and then displays the sum of all the integers from 1 to n

# How to do?
# 1. Request numb erfrom the user and store
# 2. Calculate sum of first n integers using known formula
# 3. Output the final total

"""

### Script 1: 
n = int(input("Please enter n: "))
sum_to_n = 0
for i in range(n):
    sum_to_n = sum_to_n + i
    print(f"the sum from 1 to {n} is {sum_to_n}")

# n = 5
# sum of the number from 0,1,2,3,4 = 10 (starts from 0 to the number before n)
#%%   
    
#%%

### Script 2:
n = int(input("Please enter n: "))
sum_to_n = 0
for i in range(1,n+1):
    sum_to_n = sum_to_n + i # (n=3,  = 6)
    print(f"the sum from 1 to {n} is {sum_to_n}")
    

# n = 5
# sum of the number from 0,1,2,3,4,5 = 15 (starts from 0 to the number before n+1, which is n)

#%%

"""
Task 2: Coin
Calculate required coin values for change

2 pounds
1 pound
50 pence
20 pence
10 pence
5 pence
2 pence
1 pence

While condition
"""

### Script 1:

remaining_value = int(input("Please inout the required change in pence: "))

num_of_2P = 0
while remaining_value >= 200:
    num_of_2P = num_of_2P + 1
    remaining_value = remaining_value - 200
    print(f"num of 2 pounds coin: {num_of_2P}; remaining: {remaining_value}")
    
num_of_1P = 0
while remaining_value >= 100:
    num_of_1P = num_of_1P + 1
    remaining_value = remaining_value - 100
    print(f"num of 2 pounds coin: {num_of_1P}; remaining: {remaining_value}")

num_of_50p = 0
while remaining_value >= 50:
    num_of_50p = num_of_50p + 1
    remaining_value = remaining_value - 50
    print(f"num of 2 pounds coin: {num_of_50p}; remaining: {remaining_value}")
    
#%%    

### Script 2:
    
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

### Script 3:

# Change-making: shortest clean version
"""
ใช้ divmod(remaining, d) → ได้ทั้ง จำนวนเหรียญ (remaining // d) และ เศษที่เหลือ (remaining % d) ในครั้งเดียว
"""
remaining = int(input("Please input the required change in pence: "))

denoms = [200, 100, 50, 20, 10, 5, 2, 1]   # £2, £1, 50p, ... , 1p
counts = {}

for d in denoms:
    counts[d], remaining = divmod(remaining, d)

# display
labels = {200:"£2", 100:"£1", 50:"50p", 20:"20p", 10:"10p", 5:"5p", 2:"2p", 1:"1p"}
for d in denoms:
    print(f"{labels[d]}: {counts[d]}")
    
#%%    

### Script 4: 
    
"""
ใช้ divmod(remaining, d) → ได้ทั้ง จำนวนเหรียญ (remaining // d) และ เศษที่เหลือ (remaining % d) ในครั้งเดียว
not show coin = 0
"""    
# 💷 Compact UK coin change calculator
remaining = int(input("Please input the required change in pence: "))

# เหรียญและธนบัตร (หน่วยเป็น pence)
denoms = [200, 100, 50, 20, 10, 5, 2, 1]
labels = {200:"£2", 100:"£1", 50:"50p", 20:"20p",
          10:"10p", 5:"5p", 2:"2p", 1:"1p"}

print("\nBreakdown of change:")
for d in denoms:
    count, remaining = divmod(remaining, d)
    if count > 0:
        print(f"{labels[d]} coins: {count}")

#%%




