import math


def end_corona(recovers, new_cases, active_cases):
    return math.ceil(active_cases / (recovers - new_cases))


print(end_corona(4000, 2000, 77000))  # ➞ 39
print(end_corona(3000, 2000, 50699))  # ➞ 51
print(end_corona(30000, 25000, 390205))  # ➞ 79
