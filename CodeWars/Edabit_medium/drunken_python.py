# Python got drunk and the built-in functions str() and int() are acting odd:
#
# str(4) ➞ 4
# str("4") ➞ 4
# int("4") ➞ "4"
# int(4) ➞ "4"
# You need to create two functions to substitute str() and int().
# A function called int_to_str() that converts integers into strings and a function called str_to_int()
# that converts strings into integers.

def convert_type(num):
    return int(num) if type(num) is str else str(num)

print(convert_type('7'))                # ➞ 7
print(convert_type(7))                  # ➞ '7'
print(convert_type(type('7')))          # ➞ Str
print(convert_type(type(7)))            # ➞ Int
