# Complete the function that accepts a string parameter,
# and reverses each word in the string. All spaces in the string should be retained.

def reverse_word(text):
    return '_'.join(word[::-1] for word in text.split(' '))


print(reverse_word("This is an example!"))
print(reverse_word("double  spaces"))
print(reverse_word("The quick brown fox jumps over the lazy dog."))


def uppercase_letter(password):
    return ''.join(upper_letter.upper() for upper_letter in password)


print(uppercase_letter("This is an example!"))

# 1) create new string separated by space
# 2) join all it
# 3) reverse the word
# 4) for each split the word
