def next_in_line(lst, n):
    if lst != []:
        lst.remove((lst[0]))
        lst.append(n)
        return lst
    else: return "No list has been selected"

print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([], 6))
