def isPosDiv(num: int) -> bool:
    if num % 10 == 0:
        return True
    return False

print(isPosDiv(10)) #True
print(isPosDiv(-1)) #False
print(isPosDiv(5))  #False