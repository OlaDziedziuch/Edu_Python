# slice[:]  copying all list
# slice[start,end] -> start - included, end - excluded
# slice can be negative [:-1]
# my_list[:end] -> not needed [0:end]
# my_list[start:][len(my_list)]
# del my_list[start:end] -> it is not creating a new list
# elem in my_list - True/False
# elem not in my_list -> True/False

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list.sort()
new_list = my_list[0:1] + my_list[4:5] + my_list[7:10]

print("The list with unique elements only:")
print(new_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in my_list:
    if my_list[0:] == my_list[0:]:
        del my_list[i]

print("The list with unique elements only:")
print(my_list)

rev_my_list = my_list[::-1]
print(rev_my_list)

