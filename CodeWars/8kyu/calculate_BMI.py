# Write function bmi that calculates body mass index (bmi = weight / height2).
#if bmi <= 18.5 return "Underweight"
#if bmi <= 25.0 return "Normal"
#if bmi <= 30.0 return "Overweight"
#if bmi > 30 return "Obese"


def count_bmi(weight, height):
    bmi = weight / height ** 2
    return 'Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 'Overweight' if bmi <= 30.0 else "Obese"

print(count_bmi(50, 1.80))                  # ➞ Underweight
print(count_bmi(80, 1.80))                  # ➞ Normal
print(count_bmi(90, 1.80))                  # ➞ Overweight
print(count_bmi(110, 1.80))                 # ➞ Obese
print(count_bmi(50, 1.50))                  # ➞ Normal

