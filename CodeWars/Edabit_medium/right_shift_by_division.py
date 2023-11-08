# The right shift operation is similar to floor division by powers of two.
#
# Sample calculation using the right shift operator ( >> ):
#
# 80 >> 3 = floor(80/2^3) = floor(80/8) = 10
# -24 >> 2 = floor(-24/2^2) = floor(-24/4) = -6
# -5 >> 1 = floor(-5/2^1) = floor(-5/2) = -3
# Write a function that mimics (without the use of >>) the right shift operator
# and returns the result from the two given integers.

def shift_to_right(x, y):
    return x // pow(2, y)

print(shift_to_right(80, 3))                # ➞ 10
print(shift_to_right(-24, 2))               # ➞ -6
print(shift_to_right(-5, 1))                # ➞ -3
print(shift_to_right(4666, 6))              # ➞ 72
print(shift_to_right(3777, 6))              # ➞ 59
print(shift_to_right(-512, 10))             # ➞ -1
