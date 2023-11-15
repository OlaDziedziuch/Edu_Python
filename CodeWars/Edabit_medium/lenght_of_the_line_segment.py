# Write a function that takes coordinates of two points on a two-dimensional
# plane and returns the length of the line segment connecting those two points.

import math
def line_length(dot1, dot2):
    sub_square_dot1 = pow(dot2[0] - dot1[0], 2)
    sub_square_dot2 = pow(dot2[1] - dot1[1], 2)
    sum = sub_square_dot1 + sub_square_dot2
    return math.sqrt(sum).__round__(2)


print(line_length([22, 11], [15, 7]))       # ➞ 8.06
print(line_length([0, 0], [0, 0]))          # ➞ 0
print(line_length([0, 0], [1, 1]))          # ➞ 1.41

