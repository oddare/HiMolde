list = []

for x in range(10):
    y = (x)*0.25
    if y:
        list += [True, y]
    else:
        list += [False, y]

print(list)