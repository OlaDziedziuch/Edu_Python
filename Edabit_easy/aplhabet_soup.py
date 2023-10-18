def alphabet_soup(txt):
    return "".join(sorted(txt))

print(alphabet_soup("hello"))               # ➞ ehllo
print(alphabet_soup("edabit"))              # ➞ abdeit
print(alphabet_soup("hacker"))              # ➞ acehkr
print(alphabet_soup("geek"))                # ➞ eegk
print(alphabet_soup("javascript"))          # ➞ aacijprstv
