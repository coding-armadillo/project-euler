# 10001st prime


# Solution 1
num = 2
primes = []


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


while len(primes) != 10001:
    if is_prime(num) == True:
        primes.append(num)
    num = num + 1
print(primes[10000])


# Solution 2
from primePy import primes

a = primes.first(10001)
print(a[-1])
