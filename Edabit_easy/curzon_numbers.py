def curzon_numbers(num):
    result_1 = 2 * num + 1
    result_2 = 2 ** num + 1
    return result_2 % result_1 == 0

print(curzon_numbers(5))            # ➞ True
print(curzon_numbers(10))           # ➞ False
print(curzon_numbers(14))           # ➞ True

