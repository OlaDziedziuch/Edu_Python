def days_in_month(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        return 28
    return 30


def day_of_year(year, month, day):
    days = 0
    for i in range(1, month):
        md = days_in_month(year, i)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

def test_day_of_the_year():
    test_years = [1900, 2000, 2016, 1987]
    test_months = [12, 2, 1, 11]
    test_days = [31, 16, 19, 5]
    test_results = [365, 47, 19, 309]
    for i in range(len(test_years)):
        yr = test_years[i]
        mo = test_months[i]
        da = test_days[i]
        print(yr, mo, da, "➞", end="")
        result = day_of_year(yr, mo, da)
        if result == test_results[i]:
            print("Passed")
        else:
            print("Failed")

test_day_of_the_year()


