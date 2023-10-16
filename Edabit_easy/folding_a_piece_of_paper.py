import math

def num_layers(n):
    return (math.pow(2, n-1))/1000

print(num_layers(1))            # ➞ 0.001
print(num_layers(4))            # ➞ 0.008
print(num_layers(21))           # ➞ 1048.576
