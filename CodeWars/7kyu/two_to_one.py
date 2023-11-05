# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.

def longest(str1, str2):
     return "".join(sorted([element for element in set(str1 + str2)]))

def longest_refactored(str1, str2):
    return "".join(sorted(set(str1 + str2)))

print(longest("aretheyhere", "yestheyarehere"))                             # ➞ aehrsty
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))       # ➞ abcdefghilnoprstu
print(longest("inmanylanguages", "theresapairoffunctions"))                 # ➞ acefghilmnoprstuy
print(longest("inmanylanguages", "inmanylanguages"))                        # ➞ aegilmnsuy


print(longest_refactored("aretheyhere", "yestheyarehere"))                             # ➞ aehrsty
print(longest_refactored("loopingisfunbutdangerous", "lessdangerousthancoding"))       # ➞ abcdefghilnoprstu
print(longest_refactored("inmanylanguages", "theresapairoffunctions"))                 # ➞ acefghilmnoprstuy
print(longest_refactored("inmanylanguages", "inmanylanguages"))                        # ➞ aegilmnsuy
