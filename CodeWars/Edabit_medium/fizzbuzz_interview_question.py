# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
#
# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in
# the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5.

def fizz_buzz(num):
    divided_by_3 = "Fizz"
    divided_by_5 = "Buzz"

    if num % 3 == 0 and num % 5 == 0:
        return divided_by_3 + divided_by_5
    if num % 3 == 0:
        return divided_by_3
    if num % 5 == 0:
        return divided_by_5
    if num % 3 != 0 or num % 5 != 0:
        return str(num)


print(fizz_buzz(3))                 # ➞ Fizz
print(fizz_buzz(5))                 # ➞ Buzz
print(fizz_buzz(15))                # ➞ FizzBuzz
print(fizz_buzz(4))                 # ➞ 4

def test_fizz_buzz():
    fizz_buzz_test_data = [3, 5, 15, 4]
    fizz_buzz_test_results = ["Fizz", "Buzz","FizzBuzz", "4"]
    for i in range(len(fizz_buzz_test_data)):
        txt = fizz_buzz_test_data[i]
        print("Test for:", txt, "➞", end="")
        result = fizz_buzz(txt)
        if result == fizz_buzz_test_results[i]:
            print("Passed")
        else:
            print("Failed")

test_fizz_buzz()

