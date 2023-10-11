import unittest

def relation_to_luke(name):
    d = {"Darth Vader": "dad",
         "Leia": "sister",
         "Han": "brother in law",
         "R2D2": "droid"}

    name = d.get(name)
    return ("Luke I am your {}".format(name))

print(relation_to_luke("Darth Vader"))      #  ➞ Luke I am your dad
print(relation_to_luke("Leia"))             #  ➞ Luke I am your sister
print(relation_to_luke("Han"))              #  ➞ Luke I am your brother in law
print(relation_to_luke("R2D2"))             #  ➞ Luke I am your droid
