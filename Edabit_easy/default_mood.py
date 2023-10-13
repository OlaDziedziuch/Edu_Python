def default_mood(m='neutral'):
    return 'Today, I am feeling {}'.format(m)

print(default_mood("happy"))            # ➞ "Today, I am feeling happy"
print(default_mood("sad"))              # ➞ "Today, I am feeling sad"
print(default_mood())                   # ➞ "Today, I am feeling neutral"


