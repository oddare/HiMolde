def boxmaker(n: int, a: int, b: int):
    box = ''
    for i in range(0, n):
        box += '*'
    print(box)

boxmaker(8, 1, 4)
