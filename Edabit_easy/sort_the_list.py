def sort_the_list(lst, s):
    if s == "Asc":
        return sorted(lst)
    if s == "Des":
        return lst[::-1]
    if s == "None":
        return lst

print(sort_the_list([4, 3, 2, 1], "Asc"))
print(sort_the_list([7, 8, 11, 66], "Des"))
print(sort_the_list([1, 2, 3, 4], "None"))

