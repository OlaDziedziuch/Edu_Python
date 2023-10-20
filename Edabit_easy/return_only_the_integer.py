def return_only_integer(lst):
    return [i for i in lst if isinstance(i, int) and not isinstance(i, bool)]

print(return_only_integer([9, 2, "space", "car", "lion", 16]))
print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
print(return_only_integer(["String",  True,  3.3,  1]))
