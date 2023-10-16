def filter_list(l):
    return [i for i in l if type(i) == int]

print(filter_list([1, 2, 3, "a", "b", 4]))                          # ➞ [1, 2, 3, 4]
print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))      # ➞ [0, 1729]
print(filter_list(["Nothing", "here"]))                             # ➞ [] 
