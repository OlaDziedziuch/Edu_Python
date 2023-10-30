# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    number = [i for i in str(s)]
    del number[0]
    del number[-1]
    return "".join(number)

print(remove_char("Tadziu"))        # ➞ adzi
print(remove_char("Excellent"))     # ➞ xcellen
print(remove_char("Fabulous"))      # ➞ abulou

