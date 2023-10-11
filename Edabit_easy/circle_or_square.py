import math

def circle_or_square(rad, area):
    return math.pi * rad ** 2 > area

print(circle_or_square(16, 625))        # ➞ True
print(circle_or_square(5, 100))         # ➞ False
print(circle_or_square(8, 144))         # ➞ True


