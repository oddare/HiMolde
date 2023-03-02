def checkSum(a: int, b: int, c: int) -> bool:
    if (a + b) >= c:
        return True
    return False


print(checkSum(-124, -18, 10))