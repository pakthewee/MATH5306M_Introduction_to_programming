#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 23:28:13 2025

@author: paktheweerangthong
"""

"""
Task 6: Is a Number Prime?
"""
# Import isqrt from math to compute the square roots
from math import isqrt
        
## Function to determine the input number is Prime or not

def is_prime_number(n):
    """
    Check if a given integer n is a prime number.
    A prime number is an integer greater than 1 that is only divisible by 1 and itself.
    Returns True if n is prime, otherwise False.
    """
    if n <= 1:
        print(f"False: the input number {n} is NOT a Prime Number")
        return False
    
    # If the input number (n) > 1, use a for loop to check whether the number is prime
    else:
        is_prime = True
        
        # Get the divisor, starting from 2 up to the integer square root of n (+1 for range)
        # Start with the first prime number, 2
        for d in range(2, isqrt(n) + 1):
            modular = n % d # remainder from the division

            # If there is no remainder, n can be divided exactly -> not a prime number
            if modular == 0:
                is_prime = False

                break
                
        if is_prime:
            print(f"True: the input number {n} is a Prime Number")
            return True
        else:
            print(f"False: the input number {n} is NOT a Prime Number")
            return False



### Main Program
if __name__ == "__main__":
    print("Check the Prime Number:\n")
    chk1 = is_prime_number(0.5) # is NOT a Prime Number
    chk2 = is_prime_number(1) # is NOT a Prime Number
    chk3 = is_prime_number(2) # is a Prime Number
    chk4 = is_prime_number(4) # is NOT a Prime Number
    chk5 = is_prime_number(13) # is a Prime Number
    
    print(chk1)
    print(chk2)
    print(chk3)
    print(chk4)
    print(chk5)

