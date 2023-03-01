DNA = 'ATGCTTCAGAAAGGTCTTACG'
nucleotide = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}

for x in DNA:
    nucleotide[x] += 1

print(nucleotide)