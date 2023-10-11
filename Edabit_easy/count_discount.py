import math

def count_discount(price, discount):
    return round(price - (price * discount)/ 100)

print(count_discount(100,90))       # ➞ 10
print(count_discount(1500,50))      # ➞ 750
print(count_discount(89,20))        # ➞ 71
print(count_discount(100,75))       # ➞ 25

