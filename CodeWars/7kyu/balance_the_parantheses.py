# Your job is to fix the parentheses so that all opening and closing parentheses (brackets) have matching c\
# counterparts. You will do this by appending parenthesis to the beginning or end of the string. The result should
# be of minimum length. Don't add unnecessary parenthesis.
#
# The input will be a string of varying length, only containing '(' and/or ')'.

def fix_parentheses(str):
    while '()' in str:
        str = str.replace('()', '')
    first_paranthese = str.count(')')
    second_paranthese = str.count('(')
    str = first_paranthese * '(' + str + second_paranthese * ')'
    return str

print(fix_parentheses(')('))                        # ➞ ()()
print(fix_parentheses('))))(()('))                  # ➞ (((())))(())
