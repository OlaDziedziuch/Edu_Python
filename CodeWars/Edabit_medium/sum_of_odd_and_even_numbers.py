# Write a function that takes a list of numbers and returns a list with two elements:
#
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.

def sum_of_odd_and_even(lst):
    even_total = 0
    odd_total = 0

    for number in lst:
        if number % 2 == 0:
            even_total = even_total + number
        else:
            odd_total = odd_total + number

    return [odd_total, even_total]

print(sum_of_odd_and_even([1, 2, 3, 4, 5, 6]))              # ➞ [9, 12]
print(sum_of_odd_and_even([-1, -2, -3, -4, -5, -6]))        # ➞ [-9, -12]
print(sum_of_odd_and_even([0, 0]))                          # ➞ [0, 0]
