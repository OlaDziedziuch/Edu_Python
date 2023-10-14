def count_ones(num):
    binary_str = str(bin(num))[2:]
    return binary_str.count("1")


print(count_ones(999))              #➞ 8
print(count_ones(100))              #➞ 3
print(count_ones(0))                #➞ 0
