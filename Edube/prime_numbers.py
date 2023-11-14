def is_prime(num):
    print("num: ", num)
    if num == 1:
        return False
    if num == 2:
        return True
    if num > 2:
        for i in range(2, num):
            print("i: ", i)
            if num % i == 0:
                print("dividing by ", i)
                return False
    return True


print(is_prime(98435737597))
# print(is_prime(2))
# print(is_prime(8))
# print(is_prime(17))
# print(is_prime(29))
# print(is_prime(56))
# print(is_prime(49))
# print(is_prime(63))
