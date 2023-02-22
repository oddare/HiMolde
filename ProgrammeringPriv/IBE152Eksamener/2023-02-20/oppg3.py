"""
Made by Odd, 2023-02-22
"""
#Params: ["HUGO, VICTOR" , "ASIMOV, ISAAC", "URRUTIA, SEBASTIAN"], "ANA", "BARCA"
#Returns: 1

def lexDistance(list: list, spotOne: str, spotTwo: str) -> int:
    internalList = [spotOne, spotTwo]
    internalList.sort()
    list.append(spotOne)
    list.append(spotTwo)
    list.sort()
    for n in list:
        if n == internalList[0]:
            count = 0
        elif n == internalList[1]:
            return count
        else:
            count += 1


authorList = ["HUGO, VICTOR" , "ASIMOV, ISAAC", "URRUTIA, SEBASTIAN"]

lexDistance(authorList, "BARCA", "ANA")

#45min på klokka, fjern fra tidligere oppgaver