# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric
# digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    text = text.casefold()
    sum_of_repeated = {repeated: text.count(repeated) for repeated in text}
    return len([repeated for repeated in sum_of_repeated if sum_of_repeated[repeated] >= 2 ])

print(duplicate_count("aabBcde"))                       # ➞ 54321
print(duplicate_count("aabB1cde"))                      # ➞ 54321
print(duplicate_count("ABBA"))                          # ➞ 54321
print(duplicate_count("aA11"))                          # ➞ 54321
print(duplicate_count("Indivisibilities"))              # ➞ 54321
print(duplicate_count("abcdeaa"))                       # ➞ 54321
print(duplicate_count(""))                              # ➞ 54321



