visitor = {"Japanese", "Spanish"}
employees = {1020: ["English", "Norwegian"], 667: ["English"], 2212:["Spanish"]}

def canInteract ( visitor: set, employees: dict, id: int ) -> bool:
    for i in visitor:
        for n in employees[id]:
            if n == i:
                return True
    return False

print(canInteract(visitor, employees, 2212))

#10 minutter