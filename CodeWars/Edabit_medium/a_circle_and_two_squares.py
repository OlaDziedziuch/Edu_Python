# Imagine a circle and two squares: a smaller and a bigger one. For the smaller one,
# the circle is a circumcircle and for the bigger one, an incircle.
# Create a function, that takes an integer (radius of the circle)
# and returns the difference of the areas of the two squares.

import math

def square_areas_difference(r):
    return int(math.pow(r, 2) * 2)

def test_square_areas_difference():
    test_data = [5, 6, 7]
    test_result = [50, 72, 98]

    for i in range(len(test_data)):
        test = test_data[i]
        result = square_areas_difference(test)
        if result == test_result[i]:
            print("Result for", test_data[i], "is passed")
        else:
            print("Result for", test_data[i], "is failed")

print(test_square_areas_difference())
