def basic_calculator(num1, operator, num2):
    if num2 != 0:
        return eval(str(num1) + operator + str(num2))
    else: 
        return "Cannot divide by 0"

print(basic_calculator(2, "+", 2))      # ➞ 4
print(basic_calculator(2, "*", 2))      # ➞ 4
print(basic_calculator(4, "/", 4))      # ➞ 2
