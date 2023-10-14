def count_vowels(txt):
    a = txt.count("a")
    e = txt.count("e")
    i = txt.count("i")
    o = txt.count("o")
    u = txt.count("u")
    result = a + e + i + u + o
    return result


print(count_vowels("Celebration"))      # ➞ 5
print(count_vowels("Palm"))             # ➞ 1
print(count_vowels("Prediction"))       # ➞ 4

