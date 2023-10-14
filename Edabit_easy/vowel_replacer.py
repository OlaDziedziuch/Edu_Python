def replace_vowels(txt, ch):
    vowels = "aeiou"
    lst = []
    for i in txt:
        if i in list(vowels):
            lst.append(ch)
        else:
            lst.append(i)
    return "".join(lst)

print(replace_vowels("the aardvark", "#"))          # ➞ th# ##rdv#rk
print(replace_vowels("minnie mouse", "?"))          # ➞ m?nn?? m??s?
print(replace_vowels("shakespeare", "*"))           # ➞ sh*k*sp**r*
