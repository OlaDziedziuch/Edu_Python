def convert_hours_and_minutes_into_seconds(hours, minutes):
    return hours * 3600 + minutes * 60

print(convert_hours_and_minutes_into_seconds(1,3)) # ➞ 3780
print(convert_hours_and_minutes_into_seconds(2,0)) # ➞ 7200
print(convert_hours_and_minutes_into_seconds(0,0)) # ➞ 0

