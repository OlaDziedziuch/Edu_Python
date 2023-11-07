# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the
# "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears).
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

def comp(array1, array2):
    return False if None in (array1, array2) else sorted(a ** 2 for a in array1) == sorted(array2)

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))         # ➞ True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))         # ➞ False
