from typing import Tuple

def boxPrint(board: dict):
    print( f"""    1   2   3
  +---+---+---+
a | {board['a1']} | {board['a2']} | {board['a3']} |
  +---+---+---+
b | {board['b1']} | {board['b2']} | {board['b3']} |
  +---+---+---+
c | {board['c1']} | {board['c2']} | {board['c3']} |
  +---+---+---+
""")


def listInitalizer() -> dict:
    return {
        'a1': ' ',
        'a2': ' ',
        'a3': ' ',
        'b1': ' ',
        'b2': ' ',
        'b3': ' ',
        'c1': ' ',
        'c2': ' ',
        'c3': ' ',
    }


def boxChanger(coords: dict, coord: str, symbol: str):
    coords[coord] = symbol
    return boxPrint(coords)


def playerCreation() -> Tuple[str, str]:
    player_one = input(f'Please provide player 1\'s name: ')
    player_two = input(f'Please provide player 2\'s name: ')
    return player_one, player_two


def customSymbol(player: str) -> str:
    symbol = input(f'Please choose a one character long symbol, {player}: ')
    if len(symbol) > 1:
        print('That is more than one character.\nTry again...')
        return customSymbol(player)
    return symbol


def vanillaSymbol(player_one: str) -> Tuple[str, str]:
    symbol = input(f'Please decide between \'O\' or \'X\', {player_one}: ')
    if symbol == 'O':
        return symbol, 'X'
    elif symbol == 'X':
        return symbol, 'O'
    else:
        print('Illegal symbol, try again')
        return vanillaSymbol(player_one)


def symbolChoice(player_one: str, player_two: str) -> Tuple[str, str]:
    choice = input('Do you want \'custom\' or \'vanilla\' symbols? ')
    if choice == 'vanilla':
        return vanillaSymbol(player_one)
    elif choice == 'custom':
        return customSymbol(player_one), customSymbol(player_two)
    else:
        print('No valid input given...')
        return symbolChoice(player_one, player_two)


def gameInit() -> "list[dict]":
    player_one, player_two = playerCreation()
    symbol_one, symbol_two = symbolChoice(player_one, player_two)
    return [
        {'name': player_one, 'symbol': symbol_one, 'score': 0},
        {'name': player_two, 'symbol': symbol_two, 'score': 0},
    ]


def updateScore(playerList: "list[dict]", winner: str) -> "list[dict]":
    for player in playerList:
        if player['name'] == winner:
            player['score'] += 1
    return playerList


def validTurnChecker(player: str, board: dict, coord: str) -> bool:
    print(board[coord])
    if board[coord] ==  ' ':
        return True
    return False


def playerTurn(player: str, board: dict, symbol: str) -> dict:
    coordinate = input(f'Which place on the board do you want to take, {player}? ')
    if validTurnChecker(player, board, coordinate):
        return boxChanger(board, coordinate, symbol)
    print('That slot is already taken, try again')
    return playerTurn(player, board, symbol)


def gameLoop():
    playerList = gameInit()
    baseBoard = listInitalizer()
    print(baseBoard)
    baseBoard = playerTurn(playerList[0]['name'], baseBoard, playerList[0]['symbol'])
    print(baseBoard)
    baseBoard = boxChanger(baseBoard, playerTurn(playerList[0]['name'], baseBoard, playerList[0]['symbol']), playerList[0]['symbol'])
    print(baseBoard)


boxPrint(listInitalizer())
#print(gameLoop())
#print(gameInit())
#print(customSymbol('John'))
#print(boxChanger(listInitalizer(), 'a1', 'X'))