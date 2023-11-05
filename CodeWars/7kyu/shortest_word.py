# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
# longest word are added too.

def find_short(s):
    return min(len(word) for word in s.split())

def find_long(l):
    return max(len(word) for word in l.split())

print(find_short("bitcoin take over the world maybe who knows perhaps"))                    # ➞ 3
print(find_short("turns out random test cases are easier than writing out basic ones"))     # ➞ 3
print(find_short("lets talk about javascript the best language"))                           # ➞ 3


print(find_long("bitcoin take over the world maybe who knows perhaps"))                    # ➞ 7
print(find_long("turns out random test cases are easier than writing out basic ones"))     # ➞ 7
print(find_long("lets talk about javascript the best language"))                           # ➞ 10
