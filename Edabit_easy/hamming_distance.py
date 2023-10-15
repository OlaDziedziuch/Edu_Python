def hamming_distance(txt1, txt2):
    start = 0
    for x1, x2 in zip(txt1, txt2):
        if x1 != x2:
            start += 1
    return start

print(hamming_distance("abcde", "bcdef"))           #  ➞ 5
print(hamming_distance("abcde", "abcde"))           #  ➞ 0
print(hamming_distance("strong", "strung"))         #  ➞ 1
