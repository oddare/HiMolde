DNA = 'ATGCTTCAGAAAGGTCTTACG'
RNA = ''

for x in DNA:
    if x == 'T':
        RNA += 'U'
    else:
        RNA += x

print(RNA)