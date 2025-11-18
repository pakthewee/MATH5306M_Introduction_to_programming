#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 23:25:21 2025

@author: paktheweerangthong
"""

"""
Task 1: Median of Three Values
"""

# Build a function get_median to compute the median of three numbers
def get_median(n1, n2, n3):
    
    # Create a list from the input numbers
    list_n = [n1,n2,n3]
    
    # Sort the list number by acsending order
    sort_list_n = sorted(list_n)
    
    # Find median position
    # Use n//2 to find the middle index as an integer (not a float)
    # This works correctly when the number of inputs is odd
    i = len(sort_list_n) // 2
    median = sort_list_n[i]
    
    print(f"The input numbers are: {n1}, {n2}, and {n3}")
    print(f"The sorted numbers of the input number are: {sort_list_n}")
    print(f"The median value is: {median}")
    
    return median



### Main Program
if __name__ == "__main__":
    print("Check the Median of three values:\n")
    chk1 = get_median(3, 7, 2) # the median is 3
    chk2 = get_median(6.2, 4.5, 10.7) # the median is 6.2
    
    print(chk1)
    print(chk2)


### Main program, version input the number
# n1 = float(input("please enter number 1: "))
# n2 = float(input("please enter number 2: "))
# n3 = float(input("please enter number 3: "))


# # Get function get_median()
# df_median = get_median(n1, n2, n3)