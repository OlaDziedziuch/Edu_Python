# Write a program that finds the summation of every
# number from 1 to num. The number will always be a positive integer greater than 0.

def summation(num):
    return int(num * (num + 1) / 2)

print(summation(1))             # ➞ 1
print(summation(8))             # ➞ 36
print(summation(22))            # ➞ 253
print(summation(100))           # ➞ 5050
print(summation(213))           # ➞ 22791
