def daisyGame(petals: int) -> int:
    return ((petals + 1) % 2) + 1

print(daisyGame(1)) # 1
print(daisyGame(2)) # 2
print(daisyGame(3)) # 1
print(daisyGame(4)) # 2