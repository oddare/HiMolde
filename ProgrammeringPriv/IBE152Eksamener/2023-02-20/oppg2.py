def budget_OK(budget: int, participants: int) -> bool:
    price = 0
    if participants <= 12:
        price += 100
    elif participants <= 50:
        price += 120
    else:
        price += 130
    price += ((participants // 4) * 200) + (participants % 4 * 200)
    print(price)

    if budget >= price:
        return True
    else:
        return False

print(budget_OK(0, 1)) #False
print(budget_OK(700, 12)) #True
print(budget_OK(699, 12)) #False
print(budget_OK(2721, 50)) #True
print(budget_OK(2719, 50)) #False


#Ikke fullført, 20min