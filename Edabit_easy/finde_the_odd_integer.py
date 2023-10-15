def find_odd(lst):

    for i in range(0, len(lst)):
        start = 0
        for j in range(0, len(lst)):
            if lst[i] == lst[j]:
                start += 1
        if start % 2 != 0:
            return lst[i]

print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))           #  ➞ -1
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))      #  ➞ 5
print(find_odd([10]))                                           #  ➞ 10




