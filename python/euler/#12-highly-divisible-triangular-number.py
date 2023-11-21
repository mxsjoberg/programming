"""
Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers. So the 
7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms 
would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1  : 1
3  : 1,3
6  : 1,2,3,6
10 : 1,2,5,10
15 : 1,3,5,15
21 : 1,3,7,21
28 : 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

https://projecteuler.net/problem=12
"""

def triangle_number(number): return sum(list(range(number + 1)))

# test (slow)

def factors(factor_lst, number):
    # append known factors
    factor_lst.append(number)
    factor_lst.append(number / 2)
    factor_lst.append(1)
    # set first factor (no factor larger than number / 2)
    factor = number / 2 - 1
    while factor > 1:
        if number % factor == 0: factor_lst.append(factor)
        factor -= 1
    return len(factor_lst)

assert triangle_number(7) == 28
assert factors([], 28) == 6

# solution

import math

def factors_fast(factor_lst, n):
    factor = 1
    while factor <= math.sqrt(n):
        if n % factor == 0:
            if n / factor == factor: factor_lst.append(factor)
            else:
                factor_lst.append(factor)
                factor_lst.append(int(n / factor))
        factor = factor + 1
    return len(factor_lst)

assert factors_fast([], 28) == 6

MAX_RANGE = 15000
MIN_LEN = 500

result = 0

for n in range(MAX_RANGE):
    tn = triangle_number(n)
    f = factors_fast([], tn)
    if f > MIN_LEN:
        result = tn, f
        break

print(result[0])
# 76576500