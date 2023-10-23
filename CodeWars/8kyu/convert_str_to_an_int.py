# We need a function that can transform a string into a number. What ways of achieving this do you know?
#
# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

def convert_it(number):
    return int(number)

print(convert_it("1234"))               # ➞ 1234
print(convert_it("605"))                # ➞ 605
print(convert_it("1405"))               # ➞ 1405
print(convert_it("-7"))                 # ➞ -7

print(type(convert_it(3)))              # ➞ <class_'int'>
