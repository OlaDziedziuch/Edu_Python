def instant_jazz(lst):
    new_lst = []
    for element in lst:
        if element.endswith("7"):
            new_lst.append(element)
        else:
            new_lst.append(element + "7")
    return new_lst


print(instant_jazz(["G", "F", "C"]))                            # ➞ ['G7', 'F7', 'C7']
print(instant_jazz(["Dm", "G", "E", "A"]))                      # ➞ ['Dm7', 'G7', 'E7', 'A7']
print(instant_jazz(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))     # ➞ ['F7', 'E7', 'A7', 'Ab7', 'Gm7', 'C7']
