def missing_num(lst):

    new_lst = []
    for i in range(1, 11):
	    new_lst += [i]
	    for j in new_lst:
			    if j in lst:
				    continue
			    else:
				    return j


print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))            # ➞ 5
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))             # ➞ 10
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))            # ➞ 7

