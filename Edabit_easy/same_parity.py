def same_parity(num):
    var = 0
    for i in str(num):
        var += int(i)
    return True if (var % 2 == 0 and num % 2 == 0) or (var % 2 != 0 and num % 2 != 0) else False


print(same_parity(243))
print(same_parity(12))
print(same_parity(3))

