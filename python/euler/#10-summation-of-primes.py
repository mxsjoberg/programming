"""
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10
"""

import numpy as np

# sieve of eratosthenes
def SOE(primelst, MAX_SIZE=10):
    is_prime = np.ones(MAX_SIZE)
    
    prime = 2
    while (prime * prime) < MAX_SIZE:
        if is_prime[prime] == True:
            i = (prime * prime)
            while i < MAX_SIZE:
                is_prime[i] = 0
                i += prime
        prime += 1

    prime = 2
    while prime < MAX_SIZE:
        if is_prime[prime]: primelst.append(prime)
        prime += 1

    return primelst

assert(sum(SOE([], 10)) == 17)

result = SOE([], 2000000)
print(sum(result)) # 142913828922