def is_valid_PIN(pin):
    numeric = pin.isnumeric()
    if pin != "":
        if len(pin) == 4 or len(pin) == 6:
            return numeric
        else:
            return not numeric
    else: return False


print(is_valid_PIN("1234"))             # ➞ True
print(is_valid_PIN("12345"))            # ➞ False
print(is_valid_PIN("123456"))           # ➞ True
print(is_valid_PIN("a234"))             # ➞ False
print(is_valid_PIN(""))                 # ➞ False
