"""
Made by Odd, 2023-02-22

# Status: Fullført
# Brukt: 48 minutter (30 på boxmaker() og 18 på try2())
"""
def boxmaker(n: int, a: int, b: int): #Defunct, doesn't work, confused myself
    box = []
    box += ['*']*n + ['\n']
    for i in range(n-2):
        box += ['*']+[' ']*(n) + ['*'] + ['\n']
    box += ['*']*n
    print(box)
    aUse = (a + 1) + (a // (n - 2))
    bUse = b + 1
    coordinate = aUse * bUse * (n + 1)
    box[coordinate] = 'x'

    boxShow = ''
    for i in box:
        boxShow += i
    print(boxShow)

#boxmaker(8, 1, 1)


def try2(n: int, a: int, b: int):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                print('* ', end='')
            elif i == a and j == b:
                print('x ', end='')
            else:
                print('  ', end='')
        print()


try2(8, 1, 4)