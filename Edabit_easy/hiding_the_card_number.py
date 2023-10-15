def cart_hide(card):
    code = card[0:int(len(card[:-4]))]
    last_four = card[-4:]

    for i in code:
        code = code.replace(i, "*")
    return code + last_four

print(cart_hide('1234123456785678'))            # ➞ ************5678
print(cart_hide("8754456321113213"))            # ➞ ************3213
print(cart_hide("35123413355523"))              # ➞ **********5523
