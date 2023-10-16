def add_indexes(lst):
    result = [i for i, c in enumerate(lst)]
    return [res_1 + res_2 for (res_1, res_2) in zip(lst, result)]

print(add_indexes([0, 0, 0, 0, 0]))             # ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5]))             # ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1]))             # ➞ [5, 5, 5, 5, 5]
