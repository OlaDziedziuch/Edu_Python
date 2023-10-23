# Complete the solution so that it returns true
# if the first argument(string) passed in ends with the 2nd argument (also a string).

def add_end(txt, end):
    return txt.endswith(end)

print(add_end('abc', 'bc'))             # ➞ True
print(add_end('abc', 'd'))              # ➞ False
