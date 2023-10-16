def double_char(txt):
    n = 2
    return ''.join([char*n for char in txt])

print(double_char("String"))                # ➞ "SSttrriinngg"
print(double_char("Hello World!"))          # ➞ HHeelllloo  WWoorrlldd!!
print(double_char("1234!_ "))               # ➞ 11223344!!__
