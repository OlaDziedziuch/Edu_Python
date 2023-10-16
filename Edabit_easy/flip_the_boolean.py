def reverse(arg):
    return not arg if isinstance(arg, bool) else "Boolean expected"

print(reverse(True))            # ➞ False
print(reverse(False))           # ➞ True
print(reverse(0))               # ➞ Boolean expected
print(reverse("0"))             # ➞ Boolean expected
