# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the
# "instructions" for the development and functioning of living organisms.

def DNA_strand(dna):
    dna_conversion = {
        "A" : "T",
        "T" : "A",
        "U" : "A",
        "G" : "C",
        "C" : "G",
        "Y" : "R",
        "R" : "Y"
        }

    complementary_dna = ""

    for base in dna:
        if base in dna_conversion:
            complementary_dna += dna_conversion[base]
    return complementary_dna

print(DNA_strand("AAAA"))                   # ➞ TTTT
print(DNA_strand("ATTGC"))                  # ➞ TAACG
print(DNA_strand("GTAT"))                   # ➞ CATA


def DNA_strand_2_version(dna):
    nucleotide = {"A": "T", "T": "A", "C": "D", "D": "C"}
    return " ".join([nucleotide[x] for x in dna])

print(DNA_strand("AAAA"))                   # ➞ TTTT
print(DNA_strand("ATTGC"))                  # ➞ TAACG
print(DNA_strand("GTAT"))                   # ➞ CATA


