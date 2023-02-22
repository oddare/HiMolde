def boxmaker(n: int, a: int, b: int):
    box = []
    box += ['*']*n + ['\n']
    for i in range(n):
        box += ['*']+[' ']*(n-2) + ['*'] + ['\n']
    box += ['*']*n
    print(box)
    boxShow = ''
    for i in box:
        boxShow += i
    print(boxShow)

boxmaker(8, 1, 4)
