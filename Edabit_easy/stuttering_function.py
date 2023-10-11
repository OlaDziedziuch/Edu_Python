def stuttering_function(str):
    repeated = str[:2] + "... "
    return repeated + repeated + str + "? "

print(stuttering_function("incredible"))        # ➞ in... in... incredible?
print(stuttering_function("amazing"))           # ➞ am... am... amazing?
print(stuttering_function("outstanding"))       # ou... ou... outstanding?
