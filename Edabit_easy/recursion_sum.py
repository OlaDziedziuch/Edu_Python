def sum_numbers(n):
    return n + sum_numbers(n-1) if n != 1 else 1

print(sum_numbers(5))           # ➞ 15
print(sum_numbers(1))           # ➞ 1
print(sum_numbers(12))          # ➞ 78
