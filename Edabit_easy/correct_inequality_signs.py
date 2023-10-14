def correct_signs(txt):
    return eval(txt)

print(correct_signs("3 < 7 < 11"))              # ➞ True
print(correct_signs("13 > 44 > 33 > 1"))        # ➞ False
print(correct_signs("1 < 2 < 6 < 9 > 3"))       # ➞ True



