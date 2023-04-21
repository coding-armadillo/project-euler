# Longest Collatz sequence


# Solution 1
from tqdm import tqdm


def chain(num):
    items = 1
    while num != 1:
        if num % 2 == 1:
            num = 3 * num + 1
        else:
            num = num / 2
        items += 1
    return items


max_items = 0
n = 0

for i in tqdm(range(1, 1000000)):
    items = chain(i)
    if items > max_items:
        max_items = items
        n = i

print(n)
