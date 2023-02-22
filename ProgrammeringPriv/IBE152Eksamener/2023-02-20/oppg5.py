def boxmaker(n: int, a: int, b: int):
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
    