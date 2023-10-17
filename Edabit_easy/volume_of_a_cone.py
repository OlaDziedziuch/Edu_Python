import math

def count_cone(h, r):
    return round(1/3 * math.pi * pow(r, 2) * h, 2)

print(count_cone(3, 2))                     # ➞ 12.57
print(count_cone(15, 6))                    # ➞ 565.49
print(count_cone(18, 0))                    # ➞ 0.0
