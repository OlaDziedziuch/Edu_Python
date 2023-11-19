dictionary = {
    'apple': 'fruit',
    'cucumber': 'vegetable',
    'cookie': 'sweet'}

lst = ['food', 'beverage', 'fruit', 'apple']

# get value
print(dictionary['cucumber']) # -> vegetable
#print(dictionary['carrot']) # -> KeyError

for element in lst:
    if element in dictionary:
        print(element + " is present", sep=" ")
    else:
        print(element + " is not here", sep=" ")

for key in dictionary.keys():
    print(key + "-" + dictionary[key])


for key in sorted(dictionary.keys()):
    print(key + "-" + dictionary[key])
