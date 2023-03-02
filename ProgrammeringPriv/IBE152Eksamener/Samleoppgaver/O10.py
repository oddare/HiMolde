def daisyGame(petals: int) -> int:
    return ((petals + 1) % 2) + 1


print(daisyGame(3)) # 1
print(daisyGame(4)) # 2