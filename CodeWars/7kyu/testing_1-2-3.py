# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.
import itertools


def number(lines):
     return ["{}: {}".format(str(i + 1), c) for i, c in enumerate(lines)]

print(number(["a", "b", "c"]))                  # ➞ ['1: a', '2: b', '3: c']
print(number([]))                               # ➞ []
print(number(["c", "h", "l", "o"]))             # ➞ ['1: c', '2: h', '3: l', '4: o']
