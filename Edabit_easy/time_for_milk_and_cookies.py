def time_for_milk_and_cookies(year, month, day):
    return month == 12 and day == 24

print(time_for_milk_and_cookies(2013, 12, 24))          # ➞ True
print(time_for_milk_and_cookies(2013, 1, 23))           # ➞ False
print(time_for_milk_and_cookies(2013, 12, 24))          # ➞ True

