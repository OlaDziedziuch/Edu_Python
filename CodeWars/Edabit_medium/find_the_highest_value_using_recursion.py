# Create a function that finds the highest integer in the list using recursion.

def find_highest(lst):
    if len(lst) != 1:
        m = find_highest(lst[1:])
        return m if m > lst[0] else lst[0]
    else:
        return lst[0]


print(find_highest([-1, 3, 5, 6, 99, 12, 2]))           # ➞ 99
print(find_highest([0, 12, 4, 87]))                     # ➞ 87
print(find_highest([8]))                                # ➞ 8

