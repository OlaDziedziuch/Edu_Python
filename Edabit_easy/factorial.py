def count_factorial(base):
    if base == 1:
        return 1
    else:
        return (base * count_factorial(base - 1))

print(count_factorial(3))           # ➞ 6
print(count_factorial(5))           # ➞ 120
print(count_factorial(13))          # ➞ 6227020800

