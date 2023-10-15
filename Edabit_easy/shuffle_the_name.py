def shuffle_the_name(name):
    spl = (name.split())[::-1]
    return " ".join(spl)

print(shuffle_the_name("Donald Trump"))             # ➞ Trump Donald
print(shuffle_the_name("Rosie O'Donnel"))           # ➞ O'Donnel Rosie
print(shuffle_the_name("Seymour Butts"))            # ➞ Butts Seymour
