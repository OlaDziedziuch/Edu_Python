def calculating_damage(damage, speed, time):
    if damage > 0 and speed > 0:
        if time == "second":
            return damage * speed * 1
        if time == "minute":
            return damage * speed * 60
        if time == "hour":
            return damage * speed * 3600
    else:
        return "Invalid value"

print(calculating_damage(40, 5, "second"))          # ➞ 200
print(calculating_damage(100, 1, "minute"))         # ➞ 6000
print(calculating_damage(40, 5, "hour"))            # ➞ 720000
print(calculating_damage(0, 5, "hour"))             # ➞ Invalid value
print(calculating_damage(40, 0, "hour"))            # ➞ 720000


