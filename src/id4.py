# Largest palindrome product


# Solution 1
palindromes = []
products = []

for i in range(100, 1000):
    for o in range(100, 1000):
        products.append(i * o)

for product in products:
    is_palindrome = False
    product = str(product)
    reversed_product = []
    for c in reversed(product):
        reversed_product.append(c)
    reverse = "".join(reversed_product)
    if reverse == product:
        is_palindrome = True

    if is_palindrome == True:
        palindromes.append(int(product))

palindromes.sort()
print(palindromes[-1])


# Solution 2
num = 0
palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
print(max(palindromes))
