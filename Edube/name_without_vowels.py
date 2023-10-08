user_word = input("Describe something: ")
user_word_upper = user_word.upper()
word_without_vowels = " "

for letter in user_word_upper:
    if letter == ("A"):
        continue
    elif letter == ("E"):
        continue
    elif letter == ("I"):
        continue
    elif letter == ("O"):
        continue
    elif letter == ("U"):
        continue
    else: word_without_vowels += letter
    
print(word_without_vowels)









