"""
Write a function that receives a string s, a character c and a valid position 
in the string pos and returns a new string equal to the one received except for the 
element at position pos that is equal to c.

replace(".....", "A", 2) -> "..A.."
"""
#This was swapper
def swapper(s: str, c: str, pos: int) -> str:
    first = s[0:pos]
    end = s[pos-1: -1]
    return f'{first}{c}{end}'


print(swapper('....', 'A', 2)) # -> ..A..