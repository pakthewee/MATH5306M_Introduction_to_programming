#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 23:26:55 2025

@author: paktheweerangthong
"""

"""
Task 2: The Twelve Days of Christmas
url: https://genius.com/Christmas-songs-the-twelve-days-of-christmas-lyrics
"""


# The repetitive lyrics 1 and 2 in every verse
lr1 = "On the"
lr2 = "day of Christmas, my true love sent to me"

num_order = { 1   : "first",
              2   : "second",
              3   : "third",
              4   : "fourth",
              5   : "fifth",
              6   : "sixth",
              7   : "seventh",
              8   : "eighth",
              9   : "ninth",
              10  : "tenth",
              11  : "eleventh",
              12  : "twelfth"
              }

num_gift = {1  : "A partridge in a pear tree",
            2  : "Two turtle doves",
            3  : "Three french hens",
            4  : "Four calling birds",
            5  : "Five golden rings",
            6  : "Six geese a-laying",
            7  : "Seven swans a-swimming",
            8  : "Eight maids a-milking",
            9  : "Nine ladies dancing",
            10 : "Ten lords a-leaping",
            11 : "Eleven pipers piping",
            12 : "Twelve drummers drumming"
            }


# Loop through the 12 days of Christmas (from 1 to 12)
# i represents the current day number.
# Use the num_order dictionary to get the ordinal name (e.g., 1 -> "first", 2 -> "second", ...)
# Print a blank line (\n) to separate each verse
for i in range(1, 13): # range(start = 1, stop (before 13 is 12))
    ordinal = num_order[i]
    print("\n")
    
    # Print the opening line for this verse.
    # Example: "On the third day of Christmas, my true love sent to me"
    # Get lr1 concatenate with ordinal from num_order dictionary which are ["first", "second",...] and close with lr2
    print(f"{lr1} {ordinal} {lr2}")
    
    # Special case for day 1:
    # Only print the first gift, which is i == 1
    if i == 1:
        print(num_gift[1])
        

    # For days 2 to 12:
    # Loop backwards from i down to 1 so that we list all gifts
    # From the current day back to the first day
    # Example:
    #   i = 2  ->  j goes 2, 1
    #   i = 3  ->  j goes 3, 2, 1
    #   i = 12 ->  j goes 12,11, 10, ..., 1
    
    else:
        for j in range(i, 0, -1): #range(start, stop(i-1), step)        
                
                
            # For the final line, the original lyrics is:
            # "and a partridgr in a pear tree."
            # We need to:
            #   step 1. lowercase the first letter ("A" -> "a")
            #   step 2. add "And " in front of "step 1." and end with "." 
            
            if j == 1: 
                l_1 = num_gift[1]
                l_1 = l_1[0].lower() + l_1[1:]
                print(f"And {l_1}.")      
            else:
                # For all other lines (j > 1), just print the gift as-is
                print(num_gift[j])
            
            