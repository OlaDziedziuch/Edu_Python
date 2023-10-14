def evenly_divisible(a, b, c):
    result = 0
    for i in range(a, b + 1):
        if i % c == 0:
            result += i
    return result

print(evenly_divisible(1, 10, 3))           # ➞ 18
print(evenly_divisible(1, 10, 20))          # ➞ 0
print(evenly_divisible(1, 10, 2))           # ➞ 30

