"""Compare primality testing algorithms"""

import time
import matplotlib.pyplot as pyplot
import math



def is_prime1(n):
    """Determines if n is prime"""
    prime = True
    
    for i in range(2, n):
        if n % i == 0:
            prime = False
    return prime

"""
Function is_prime1(n)
- Starts by assuming n is prime (prime = True).
- Loops from 2 up to n-1.
- If any number divides n evenly (n % i == 0), it sets prime = False.
- Returns the result (True or False) after checking all numbers.

-> Time complexity: O(n) — very slow because it checks every possible divisor.
"""


def is_prime2(n):
    """Determine if n is prime"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

"""
Function is_prime2(n)
- Similar to is_prime1, but more efficient.
- As soon as it finds a divisor, it immediately returns False and stops looping.
- If it finishes the loop without finding one, returns True.

-> Still O(n), but faster in practice due to early exit.
"""
    

def is_prime3(n):
    """Determines if n is prime"""
    prime = True
    
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            prime = False
    return prime

"""
Function is_prime3(n)
- Checks divisors only up to √n (square root of n).
- This works because if n has a divisor larger than √n, there must be a smaller one below √n.
- Uses math.floor() to make sure the loop ends at an integer value.

-> Much faster: O(√n) instead of O(n).
"""


def is_prime4(n):
    """Determine if n is prime"""
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

"""
Function is_prime4(n)
Simplified version of is_prime3.
Doesn’t use the variable prime; instead, it returns immediately when a divisor is found.

-> Fastest and cleanest version.
"""
    

inputs = list(range(2, 1000, 5))
times1, times2, times3, times4 = ([] for _ in range(4))

for n in inputs:
    start = time.perf_counter()
    is_prime1(n)
    end = time.perf_counter()
    times1.append(end - start)

    start = time.perf_counter()
    is_prime2(n)
    end = time.perf_counter()
    times2.append(end - start)

    start = time.perf_counter()
    is_prime3(n)
    end = time.perf_counter()
    times3.append(end - start)

    start = time.perf_counter()
    is_prime4(n)
    end = time.perf_counter()
    times4.append(end - start)

# Combine all 4 graphs performance
pyplot.loglog(inputs, times1, label="is_prime1")
pyplot.loglog(inputs, times2, label="is_prime2")
pyplot.loglog(inputs, times3, label="is_prime3")
pyplot.loglog(inputs, times4, label="is_prime4")
pyplot.legend()



# Check performance for each graph
pyplot.loglog(inputs, times1, label="is_prime1")
pyplot.legend()
pyplot.show()   # ✅ แสดงกราฟแรก

pyplot.loglog(inputs, times2, label="is_prime2")
pyplot.legend()
pyplot.show()   # ✅ แสดงกราฟที่สอง

pyplot.loglog(inputs, times3, label="is_prime3")
pyplot.legend()
pyplot.show()

pyplot.loglog(inputs, times4, label="is_prime4")
pyplot.legend()
pyplot.show()


