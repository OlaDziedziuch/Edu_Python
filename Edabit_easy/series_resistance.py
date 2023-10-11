def series_resistance(lst):
    if lst.__contains__(0):
        return "Sorry, input is invalid"
    else:
        if sum(lst) <= 1:
            result = str(sum(lst))
            return result + " Ohm"
        else:
            result = str(sum(lst))
            return result + " Ohms"
        

print(series_resistance([1, 5, 6, 3]))      # ➞ 15 Ohms
print(series_resistance([16, 3.5, 6]))      # ➞ 25.5 Ohms
print(series_resistance([0.5, 0.5]))        # ➞ 1.0 Ohms
print(series_resistance([0, 0.5]))          # ➞ Sorry, input is invalid

