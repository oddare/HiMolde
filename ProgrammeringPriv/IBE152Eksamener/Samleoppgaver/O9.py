def program():
    list = [1, 2, 9362, 4, 5]
    studnum = 48234 #Not real, this is random
    index = list.index(9362)
    list.insert(index+1, studnum)
    list.pop(-1)

    print(list)