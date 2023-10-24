def convert_and_reverse(n):
    return [int(i) for i in str(n)][::-1]

print(convert_and_reverse((35231)))                 # ➞ [1, 3, 2, 5, 3]
print(convert_and_reverse((0)))                     # ➞ [0]
print(convert_and_reverse((23582357)))              # ➞ [7, 5, 3, 2, 8, 5, 3, 2]
print(convert_and_reverse((984764738)))             # ➞ [8, 3, 7, 4, 6, 7, 4, 8, 9]
