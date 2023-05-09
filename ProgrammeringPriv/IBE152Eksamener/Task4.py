def find_last_common(list1: list, list2: list) -> dict:
    common = {}

    for itemA in list1:
        for itemB in list2:
            if itemA == itemB and itemA not in common:
                pos1 = len(list1) - list1[::-1].index(itemA) - 1
                pos2 = len(list2) - list2[::-1].index(itemA) - 1
                common[itemA] = [pos1, pos2]

    return common

print(find_last_common([1, 0, 3, 4, 5, 3], [3, 4, 5 ]))
print(find_last_common([ 1, 0, 3, 4, 5], [30, 40, 50 ]))