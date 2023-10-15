def filter_list(lst):
    return [element for element in lst if isinstance(element, int)]

print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))


    # filter_list([1, 2, "a", "b"]) ➞ [1, 2]
