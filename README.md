# MATH5306M Introduction to Programming 2025/26
## Assignment 1

### Task 1: Median of Three Values

In this task, the get_median(n1, n2, n3) function is implemented to compute the median of three input values provided by user. The function first accepts three parameters including n1, n2 and n3, and store them in a list. It then applies the sorted() function to the numbers in ascending order. The middle index is determined using the expression len(sort_list_n) // 2, which divides the list length by two and rounds down to the nearest integer. Since the input size is fix at three, this approach correctly locates the median position for an odd number of elements. Finally, the function retrieves the value at this middle position from the sorted list, which represents the median, and returns it the output.


### Task 2: The Twelve Days of Christmas

In this task, I created a for loop program to display the complete lyrics of The Twelve Days of Christmas. The program begins with the repetitive opening line that appears in every verse, and it uses two dictionaries: num_order to store the ordinal numbers (e.g., first, second, third, etc.) and num_gift to store the twelve gifts mentioned in the song. The main loop runs through the twelve days of Christmas, where the variable ‘i’ represents the current day and the corresponding number of gifts. Inside this loop, another loop using the variable ‘j’ iterates backward from the latest gift on that day to the first gift.


### Task 6: Is a Number Prime?

In this task, the function is_prime_number(n) is implemented to determine whether the input integer ‘n’ is a prime number. A prime number is defined as an integer greater than 1 that is divisible only by 1 and itself. The function first checks this condition using an if statement, if the input number is less than or equal to 1, it is immediately identified as not a prime and returns ‘False’. Otherwise, when the number is greater than 1, the function initially assumes it to be prime and then verifies this assumption within a for loop. 
Referring to the concept of the Sieve of Eratosthenes, the function tests divisibility by every integer starting from 2 up to the square root of ‘n’ is not a prime number, the function then sets the flag to ‘False’ breaks out of the loop, and returns ‘False’. If no divisor is found after completing the loop, the function confirms that the number is prime and returns ‘True’.


### Task 10: Magic Dates

In this task, I created three functions to identify and display magic dates, each serving a different purpose but working together as one program. The first function, is_magic_date(d), receives a date from the user, calculates it, and returns whether it satisfies the magic date formula, where the day multiplied by the month equals the last two digits of the year. 
The second function, find_magic_dates(), checks all the dates in the 20th century and returns every magic date found within that period. It uses an if condition and calls the is_magic_date(d) function to determine whether each date is a magic date, iterating day by day from the start date to the end date by adding one day sequentially. 
The last function, check_magic_date(input_date), receives an input date from the user and converts the string into a valid date format. It also checks whether the input follows the defined “YYYY-MM-DD” pattern. If the input date is valid, the function calls is_magic_date(d) to verify whether it is a magic date, returning ‘True’ if it is, and ‘False’ otherwise.
b9ba224e0aa8" />

