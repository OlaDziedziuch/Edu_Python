secret_word = "chupacabra"
user_input = input("Check this out! ")

while user_input != secret_word:
    print("Oops!")
while user_input == secret_word:
    print("Congrats! You escaped from your faith!")
    break
