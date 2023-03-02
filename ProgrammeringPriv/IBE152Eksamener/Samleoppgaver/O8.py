def isPosDiv(num: int) -> bool:
    if num % 10 == 0:
        return True
    return False

print(isPosDiv(10))
print(isPosDiv(-1))
print(isPosDiv(5))