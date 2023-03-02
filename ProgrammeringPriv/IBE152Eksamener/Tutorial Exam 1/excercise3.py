"""
Made by Odd, 2023-02-22
Completed previously

# Status: Fullført
# Brukt: 24 minutter

You are organizing a bowling activity for a group of students and have a restricted budget.  

To enter the place, the venue charges a price of 100 NOK for a group of up to 12 people, 
120 NOK for a group from 13 up to 50 people and 130 NOK for a group of more than 50 people. 
Besides, enough bowling lines must be rented for all the students to play simultaneously. 
Each bowling line is used simultaneously by up to 4 students. 
Any number of bowling lines can be rented for 200 NOK each.
Write a function that, given the budget and the number of participants in the activity, 
returns True if the budget is enough and False otherwise. 
"""
def budget_OK(budget: int, participants: int) -> bool:
    price = 0
    if participants <= 12:
        price += 100
    elif participants <= 50:
        price += 120
    else:
        price += 130
    price += ((participants // 4) * 200) + ((participants % 4 > 0) * 200) #Explained below
    #If there is a remainder we wish to rent ONE extra alley
    #AKA: If remainder then price + 200. By checking if there is a remainder (val > 0)
    #We get True. True equals the value of 1 and we can therefor multiply by 200.
    #If it yields false we get the expression 0 * 200 and no extra value is added

    if budget >= price:
        return True
    else:
        return False


print(budget_OK(0, 1)) #False
print(budget_OK(700, 12)) #True
print(budget_OK(699, 12)) #False
print(budget_OK(2721, 50)) #True
print(budget_OK(2719, 50)) #False