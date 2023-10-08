def return_sum_of_two_numbers():
   a = int(input("Enter number: "))
   b = int(input("Enter number: "))
   sum = a + b
   return "The sum is" + " " + str(sum)

# print(return_sum_of_two_numbers())

def return_sum_of_two_numbers_2(x,y):
   return "The sum is" + " " + str(x + y)

print(return_sum_of_two_numbers_2(3,2))     # -> 5
print(return_sum_of_two_numbers_2(-3,-6))   # -> -9
print(return_sum_of_two_numbers_2(7,3))     # -> 10





