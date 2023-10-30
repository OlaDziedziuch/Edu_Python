# Your task is to make a function that can take any non-negative integer as an argument and return it
# with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
#
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):
    number = [int(i) for i in str(num)]
    sorted_numbers = sorted(number, reverse=True)
    return int(''.join(map(str, sorted_numbers)))


print(descending_order(12345))                      # ➞ 54321
print(descending_order(145263))                     # ➞ 654321
print(descending_order(123456789))                  # ➞ 987654321

