# Sum square difference


# Solution 1
a = 0
b = 0

for i in range(1, 101):
    a = a + pow(i, 2)

for i in range(1, 101):
    b = b + i
b = pow(b, 2)

print(b - a)
