kms_per_mile = 1609.344
liters_per_gallon = 3.785411784
kilometres = 100_000

def liters_100km_to_miles_gallon(liters):
    return liters_per_gallon /(kms_per_mile * liters) * kilometres

def miles_gallon_to_liters_100km(miles):
    return (liters_per_gallon / (miles * kms_per_mile)) * kilometres


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
