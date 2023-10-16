def index_of_caps(word):
    return [i for i, c in enumerate(word) if c.isupper()]

print(index_of_caps("eDaBiT"))          # ➞ [1, 3, 5]
print(index_of_caps("eQuINoX"))         # ➞ [1, 3, 4, 6]
print(index_of_caps("determine"))       # ➞ []
print(index_of_caps("STRIKE"))          # ➞ [0, 1, 2, 3, 4, 5]
print(index_of_caps("sUn"))             # ➞ [1]


# index_of_caps("eDaBiT") ➞ [1, 3, 5]
