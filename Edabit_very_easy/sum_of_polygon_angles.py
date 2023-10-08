def sum_of_polygon_angles(n):
    if n > 2:
        return  (n - 2) * 180
    else:
        return "Bad value"

print(sum_of_polygon_angles(3))     # ➞ 180
print(sum_of_polygon_angles(4))     # ➞ 360
print(sum_of_polygon_angles(6))     # ➞ 720

