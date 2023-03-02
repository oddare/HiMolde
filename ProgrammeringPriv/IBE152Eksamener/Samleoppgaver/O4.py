def listCheck(numlist: list, num: int) -> int:
    if num in numlist:
        return numlist.index(num)
    return -1


print(listCheck([1, 2, 3, 4, 5], 3))