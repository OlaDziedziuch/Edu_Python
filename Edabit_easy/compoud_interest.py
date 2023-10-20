import math

def compound_interest(p, t, r, n):
    return round(p * math.pow((1+r/n), (n * t)), 2)

print(compound_interest(10000, 10, 0.06, 12))               # ➞ 18193.97
print(compound_interest(3500, 15, 0.1, 4))                  # ➞ 15399.26
print(compound_interest(100000, 20, 0.15, 365))             # ➞ 2007316.26
