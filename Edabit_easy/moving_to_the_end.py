def move_to_end(lst, el):
    lst.append(el)
    return lst

print(move_to_end([1, 3, 2, 4, 4, 1], 1))                   # ➞ [1, 3, 2, 4, 4, 1, 1]
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))                # ➞ [7, 8, 9, 1, 2, 3, 4, 9]
print(move_to_end(["a", "a", "a", "b"], "a"))               # ➞ ['a', 'a', 'a', 'b', 'a']

