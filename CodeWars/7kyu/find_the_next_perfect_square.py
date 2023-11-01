# You might know some pretty large perfect squares. But what about the NEXT one?
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
import math

def find_next_square(sq):
    n = math.sqrt(sq)
    return int(pow(n + 1, 2)) if n == math.isqrt(sq) else -1

print(find_next_square(144))                # ➞ 169
print(find_next_square(150))                # ➞ -1
print(find_next_square(319225))             # ➞ 320356
print(find_next_square(31))                 # ➞ -1
