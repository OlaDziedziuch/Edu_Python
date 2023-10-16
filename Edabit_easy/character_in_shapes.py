def count_characters(lst):
    lst = sum(len(i) for i in lst)
    return lst

print(count_characters(
    ["###",
    "###",
    "###"]))                        #  ➞ 9

print(count_characters([
  "22222222",
  "22222222",
]))                                 #  ➞ 16

print(count_characters([]))         #  ➞ 0

print(count_characters(["", ""]))   #  ➞ 0
