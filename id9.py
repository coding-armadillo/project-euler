# Special Pythagorean triplet


# Solution 1
solved = False

for a in range(1, 1000):
    for b in range(1, 1000 - a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a * b * c)
            solved = True
            break
    if solved:
        break
