# Make a function that will return a greeting statement that uses an input;
# your program should return, "Hello, <name> how are you doing today?".

def return_string():
    name = str(input("What's your name? "))
    return "Hello " + name + ", how are you doing today?"

print(return_string())          # ➞ Hello {name}, how are you doing today?
