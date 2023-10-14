import math

def is_tripled(a, b, c):
    lst = [a, b, c]
    lst.sort()
    return math.pow(lst[0], 2) + math.pow(lst[1], 2) == math.pow(lst[2], 2)

print(is_tripled(3, 4, 5))          # ➞ True
print(is_tripled(13, 5, 12))        # ➞ True
print(is_tripled(1, 2, 3))          # ➞ False
