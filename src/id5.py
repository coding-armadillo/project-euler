# Smallest multiple


# Solution 1
from collections import Counter
from primePy import primes


def find_primes(n):
    prime_factors = Counter()
    for i in primes.upto(n):
        while n % i == 0:
            n /= i
            prime_factors[i] += 1
    return prime_factors


factors = Counter()
for i in range(2, 21):
    _factors = find_primes(i)
    for p in _factors:
        factors[p] = max(_factors[p], factors[p])

ans = 1
for p in factors:
    ans *= p ** factors[p]

print(ans)


# Solution 2
num = 200000000
while True:
    j = 1
    for k in range(2, 21):
        if num % k:
            j = 0
            break
    if j == 1:
        print(num)
        break
    num += 1
