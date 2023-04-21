# Largest prime factor


# Solution 1
import math

from primePy import primes

prime = primes.factors(600851475143)
print(prime[-1])


# Solution 2
def prime_factors(num):
    largest_prime_factor = 1
    while num % 2 == 0:
        largest_prime_factor = 2
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            largest_prime_factor = i
            num = num / i
    if num > 2:
        largest_prime_factor = num

    return largest_prime_factor


num = 600851475143
print(prime_factors(num))
