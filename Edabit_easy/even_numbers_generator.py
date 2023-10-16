def find_even_numbers(num):
    return [i for i in range(num) if i % 2 == 1]

print(find_even_numbers(5))           # ➞ [1, 3]
print(find_even_numbers(10))          # ➞ [1, 3, 5, 7, 9]
print(find_even_numbers(25))          # ➞  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
