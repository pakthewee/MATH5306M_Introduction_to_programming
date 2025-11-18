#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 23:30:50 2025

@author: paktheweerangthong
"""

"""
Task 10: Magic Dates
"""

from datetime import date, timedelta, datetime

### Function to identify which date is the magic date

# d is a parameter in the function which is "input date" from the user
def is_magic_date(d):
    
    """Calculate the magic date"""
    d_day = d.day # get a day from input date
    d_month = d.month # get a month from input date
    d_year_2dg = int(d.strftime("%y")) # get a 2-digit year from input date
    return d_day * d_month == d_year_2dg
    

### Function get the magic dates in 20th century
def find_magic_dates():
    
    """Date in 20th century"""
    start_date = date(1901, 1, 1) # January 1, 1901
    end_date = date(2000, 12, 31) # December 31, 2000
    d = start_date
    
    # Keep return magic dates into the list
    magic_dates = []
    
    while d <= end_date:
        
        """Check if it's a magic date"""
        # Check the magic date from function is_magic_date
        if is_magic_date(d):
            
            # Show all the magic dates in %B %d, %Y" format e.g. June 10, 1960
            print(d.strftime("%B %d, %Y"))
           
            # Store magic date and return to "%Y-%m-%d" date format
            magic_dates.append(d.strftime("%Y-%m-%d"))
        
        # Get further magic date until end_date
        d += timedelta(days=1)
    
    return magic_dates


### Funtion to get the date from user and identify that's a magic date or not
def check_magic_date(input_date):
    
    try:
        # I use YYYY-MM-DD format because it is easy for users to input the date
        # Use strptime() (string parse time) to convert string (input_date) to date object (d)
        d = datetime.strptime(input_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid format. Please use YYYY-MM-DD., e.g. 1960-06-10")
        return None
    
    # Show the input date in %B %d, %Y" format e.g. June 10, 1960
    d_display = d.strftime("%B %d, %Y")
    
    # Return True if the entered date is a Magic Date
    if is_magic_date(d):
        print(f"The entered date: {d_display} is a Magic Date")
        return True
    
    # Return False if the entered date is not a Magic Date
    else:
        print(f"The entered date: {d_display} is NOT a Magic Date")
        return False
    

# Main Program
if __name__ == "__main__":
    print("All magic dates in the 20th century:\n")
    all_magic = find_magic_dates()
    print(all_magic) # check return value --> the list of magic date

    print("\n--- Check the input date from user ---")
    chk1 = check_magic_date("1960-06-nn") # is wrong format
    chk2 = check_magic_date("1960-06-10") # is the magic date
    chk3 = check_magic_date("1960-06-11") # is not a magic date
    
    # check return value
    print(chk1) # --> None, wrong date format
    print(chk2) # --> True
    print(chk3) # --> False

