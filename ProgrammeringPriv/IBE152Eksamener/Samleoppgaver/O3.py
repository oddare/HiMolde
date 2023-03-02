def checkSum(a: int, b: int, c: int) -> bool:
    if (a + b) >= c or c % 2 == 0:
        return True
    return False


print(checkSum(-124, -18, 10))