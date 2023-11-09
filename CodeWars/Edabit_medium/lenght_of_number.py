# Create a function that takes a number num and returns its length.

def number_length(num):
    numbers = [i for i in str(num)]
    return sum(map(lambda x:1, numbers))

print(number_length(10))                # ➞ 2
print(number_length(5000))              # ➞ 4
print(number_length(0))                 # ➞ 1
