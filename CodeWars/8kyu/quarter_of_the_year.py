# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
#
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter;
# and month 11 (November), is part of the fourth quarter.

def quarter_of(month):
    if month in range(1, 3):            # ➞ 1
        return 1
    if month in range(4, 6):            # ➞ 2
        return 2
    if month in range(7, 9):            # ➞ 3
        return 3
    if month in range(10, 12):          # ➞ 4
        return 4

print(quarter_of(2))
print(quarter_of(5))
print(quarter_of(8))
print(quarter_of(11))
