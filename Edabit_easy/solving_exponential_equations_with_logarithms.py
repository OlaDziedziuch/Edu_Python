import math

def solve_for_exp(a,b):
    return round(math.log(b,a))

print(solve_for_exp(4, 1024))           # ➞ 5
print(solve_for_exp(2, 1024))           # ➞ 10
print(solve_for_exp(9, 3486784401))     # ➞ 10


