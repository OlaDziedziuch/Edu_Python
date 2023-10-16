def probability(lst, n):
    prob_high = 0
    prob_low = 0

    for i in lst:
        if i >= n:
            prob_high += 1
        else:
            prob_low += 1

    n = len(lst)
    return round((prob_high / n) * 100, 1)

print(probability([5, 1, 8, 9],6))                          # ➞ 50.0
print(probability([7, 4, 17, 14, 12, 3], 16))               # ➞ 16.7
print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))    # ➞ 70.0
