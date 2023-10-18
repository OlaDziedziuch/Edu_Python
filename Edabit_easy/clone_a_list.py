def clone(lst):
	lst = lst + [lst]
	return lst


print(clone([1, 1]))            # ➞ [1, 1, [1, 1]]
print(clone([1, 2, 3]))         # ➞ [1, 2, 3, [1, 2, 3]]
print(clone(["x", "y"]))        # ➞ ['x', 'y', ['x', 'y']]
