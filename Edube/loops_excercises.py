# Create a for loop that counts from 0 to 10,
# and prints odd numbers to the screen.

for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# Create a while loop that counts from 0 to 10,
# and prints odd numbers to the screen.

x = 1
while x < 11:
     if x % 2 != 0:
        print(x)
        x += 1


# Create a program with a for loop and a continue statement.
# The program should iterate over a string of digits, replace each
# 0 with x, and print the modified string to the screen.

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
    continue
    print(digit, end ='')

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

n = range(4) # 0,1,2,3
for num in n:
    print(num - 1)
else:
    print(num)


for i in range(0, 6, 5): #// 0,1,2,3,4,5
    print(i)

# Exercise 1: Print First 10 natural numbers using while loop

n = 0
while n < 10:
    n += 1
    print(n)

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 0
row = 5
for i in range(1, row+1, 1):
    for j in range(1, i+1):
        print(j, end="")
    print("")

# Exercise 3: Calculate the sum of all numbers from 1 to a given number

entry_number = 0
number = int(input("Enter number: "))

for i in range (1, number +1, 1):
   entry_number += i
print("Sum is:",entry_number)

# Exercise 4: Count the total number of digits in a number

counter = 0
number = int(input("Enter a number: "))
while number !=0:
    number //= 10
    counter += 1
    print(counter)

# Exercise 5: Print the following pattern
n = 0
row = 5
for i in range(1, row+1, 1):
     for j in range(1, i+1):
         print(j, end="")
     print("")
n = 5
row = 5

for i in range (0, n+1):
   for j in range (row-1,0,-1):
        print(j, end=" ")
    print()

# Exercise 6: Display numbers from -10 to -1 using for loop
a = -11
while a < 0:
     a += 1
     print(a)

# Exercise 7: Use else block to display a message “Done” after successful execution of for loop

while True:
    print("Done")
    break

# boolean values excercises

var = 1

print(var > 0)
print(not (var <= 0))

print(var != 0)
print(not (var == 0))

i = 1
j = not not i

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
# false and false or not(false) false or true
print(not(z))




