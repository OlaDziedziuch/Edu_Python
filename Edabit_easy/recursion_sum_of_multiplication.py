def recursion_sum_of_multiplication(n, ten = 10):
    while ten <= 1:
         return n * ten
    else:
         return recursion_sum_of_multiplication(n, ten-1) + (n * ten)

print(recursion_sum_of_multiplication(1))       # ➞ 55
print(recursion_sum_of_multiplication(8))       # ➞ 440
print(recursion_sum_of_multiplication(2))       # ➞ 110



