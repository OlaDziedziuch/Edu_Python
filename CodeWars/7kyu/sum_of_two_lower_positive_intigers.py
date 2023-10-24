# Create a function that returns the sum of the two lowest positive numbers given
# an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

def sum_two_smallest_numbers(numbers):
    sort_numbers = sorted(numbers)
    return sort_numbers[0] + sort_numbers[1]

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))                 # ➞ 7
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))                # ➞ 19
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))               # ➞ 30


def sum_two_smallest_numbers_refactored(numbers):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers_refactored([19, 5, 42, 2, 77]))                 # ➞ 7
print(sum_two_smallest_numbers_refactored([7, 15, 12, 18, 22]))                # ➞ 19
print(sum_two_smallest_numbers_refactored([25, 42, 12, 18, 22]))               # ➞ 30

