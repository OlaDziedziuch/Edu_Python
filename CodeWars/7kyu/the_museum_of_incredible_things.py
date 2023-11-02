# The museum of incredible dull things
# The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect,
# comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.
# However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write
# a program that tells her the ratings of the items after one removed the lowest one. Fair enough.
#
# Task
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.
#
# Don't change the order of the elements that are left.

def remove_smallest(numbers):
    if len(numbers) < 2:
        return []
    else:
        nums = numbers.copy()
        nums.remove(min(numbers))
        return nums

print(remove_smallest([1, 2, 3, 4, 5]))         # ➞ [2, 3, 4, 5]
print(remove_smallest([2, 2, 3, 1, 5]))         # ➞ [2, 2, 3, 5]
print(remove_smallest([1, 2, 3, 4, 1]))         # ➞ [2, 3, 4, 1]
print(remove_smallest([]))                      # ➞ []
