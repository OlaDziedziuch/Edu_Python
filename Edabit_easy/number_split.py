def number_split(n):
    lst = [n]
    elem_1 = round(n/2)
    elem_2 = n - elem_1
    lst = [elem_2, elem_1]
    return lst

print(number_split(4))          # ➞ [2, 2]
print(number_split(10))         # ➞ [5, 5]
print(number_split(11))         # ➞ [5, 6]
print(number_split(-9))         # ➞ [-5, -4]

