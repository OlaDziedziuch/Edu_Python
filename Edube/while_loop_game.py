secret_number = 777
# to put few-line string we can use tripple apostrophe
user_number = int(input("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""))

while user_number != secret_number:
    print("""
+==================================+
| "Ha ha! You're stuck in my loop!"|                     
+==================================+
""")
if user_number == secret_number:
    print("""
+=======================================+
| "Well done, muggle! You are free now."|                     
+=======================================+
""")
