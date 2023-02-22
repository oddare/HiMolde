"""
Made by Odd, 2023-02-22

# Status: Ferdig
# Brukt: 10 minutter
"""
def canInteract ( visitor: set, employees: dict, id: int ) -> bool:
    for i in visitor:
        for n in employees[id]:
            if n == i:
                return True
    return False

visitor = {"Japanese", "Spanish"}
employees = {1020: ["English", "Norwegian"], 667: ["English"], 2212:["Spanish"]}

print(canInteract(visitor, employees, 2212))