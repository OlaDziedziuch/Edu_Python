import math

def weight(r, h):
    return round(math.pi * r ** 2 * h/1000, 2)

print(weight(4, 10))            # ➞ 0.5
print(weight(30, 60))           # ➞ 169.65
print(weight(15, 10))           # ➞ 7.07
