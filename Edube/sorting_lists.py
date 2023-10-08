my_list = []
for i in range(5):
     my_list.insert(0,i + 1)

print(my_list)

my_list = []  #
for i in range(5):
     my_list.append(i + 1)

print(my_list)

list_to_count = [1,2,3,4,5,6,7,78,89]
total = 0

for i in range (len(list_to_count)):
    total += list_to_count[i]
print("The list's sum is", total)

for i in list_to_count:
     total += i
print("The second way to check this is: ", total)

my_list = [1,2,3,4,5,6,7,8,9,10]
lenght = len(my_list)

for i in range (len(my_list) // 2):
    my_list[i], my_list[lenght - i -1] = my_list[lenght - i -1], my_list[i]
print(my_list)

lst = ["books", "game videos", "movies"]
elements = len(lst)

lst.reverse()
print(lst)

for i in range (len(lst) //2):
    lst[i], lst[elements - i -1] = lst[elements - i -1], lst[i]
print(lst)
