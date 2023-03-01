def numCheck(sortedList: list) -> int:
    endNum = len(sortedList) + 1
    gauss = endNum / 2 * (endNum + 1)
    listSum = sum(sortedList)
    return


list = [1, 2, 3, 4, 6, 7, 8, 9, 10] #Missing 5

print(numCheck(list))