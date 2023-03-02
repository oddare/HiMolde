def budget_OK(budget: int, participants: int) -> bool:
    cost = 100
    if 5 < participants <= 10:
        cost += 20
    if participants > 10:
        cost += 30


print(budget_OK(0, 1))      #False
print(budget_OK(500, 2))    #True
print(budget_OK(300, 11))   #True
print(budget_OK(299, 11))   #False