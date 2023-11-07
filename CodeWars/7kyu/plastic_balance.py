# You will get a list with several scattered numbers
# You must check that the sum of the two values on both sides equals the sum of the rest of the list elements
# And if not, delete the two elements on the sides and check repeatedly,
# until you reach the condition checklist:
# The sum of the list without the sides = the sum of the sides
# If it never equals return an empty list []
# note: list length can be up to 500 items

def plastic_balance(lst):
    while lst and lst[0] + lst[-1] != sum(lst[1:-1]):
        lst = lst[1:-1]
    return lst

print(plastic_balance([1, 2, 3, 4, 5]))                 # ➞ []
print(plastic_balance([0, 104, 3, 101, 0, 111]))        # ➞ [104, 3, 101, 0]
print(plastic_balance([1,-1]))                          # ➞ [1, -1]
print(plastic_balance([]))                              # ➞ []

