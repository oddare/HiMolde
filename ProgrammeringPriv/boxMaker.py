"""
Provided by Arve, 2023-02-21
"""
import string
sizeX = 3
sizeY = 3
symbols = [' ', 'a', 'b']
board = [ 0, 0, 0, 0, 1, 2, 0, 2, 0]
letters = list(string.ascii_lowercase)

def getBoard(b):
    global sizeX, sizeY, symbols
    out = "    "
    for i in range(0,sizeX):
        out += (letters[i] + "   ")
    for i in range(0,sizeX):
        idx = (i+1)*(sizeX)-sizeX
        if (i== sizeY):
            break
        out+=separator(sizeX)
        items = str(i+1) +" | "+ " | ".join(map(lambda i: symbols[i], b[idx:idx+sizeX])) 
        out+= items +" | "
    out+=separator(sizeX)
    return out

def separator(len):
    out = "\n  "
    for i in (range(0,len)):
        out += "+---"
    out +="+\n"
    return out

print(getBoard(board))