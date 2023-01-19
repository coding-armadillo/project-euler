# Multiples of 3 or 5


# Solution 1
multiples = []

for number in range(1, 1000):
    if number % 5 == 0 or number % 3 == 0:
        multiples.append(number)

print(sum(multiples))
