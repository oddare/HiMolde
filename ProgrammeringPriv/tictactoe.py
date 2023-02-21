"""
Made by Odd, 2023-02-20
"""

from typing import Tuple

def boardPrint(board: dict):
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


def validTurnChecker(board: dict, coord: str) -> bool:
    if board[coord] ==  ' ':
        return True
    return False


def playerTurn(player: dict, board: dict) -> dict:
    coordinate = input(f'Which place on the board do you want to take, {player["name"]}? ')
    if validTurnChecker(board, coordinate):
        board[coordinate] = player['symbol']
        return board
    print('That slot is already taken or does not exist, try again')
    return playerTurn(player, board)


def winCheck(board: dict, symbol: str) -> bool:
    if board['a1'] == board['a2'] == board['a3'] == symbol:
        return True
    elif board['b1'] == board['b2'] == board['b3'] == symbol:
        return True
    elif board['c1'] == board['c2'] == board['c3'] == symbol:
        return True
    elif board['a1'] == board['b1'] == board['c1'] == symbol:
        return True
    elif board['a2'] == board['b2'] == board['c2'] == symbol:
        return True
    elif board['a3'] == board['b3'] == board['c3'] == symbol:
        return True
    elif board['a1'] == board['b2'] == board['c3'] == symbol:
        return True
    elif board['c1'] == board['b2'] == board['a3'] == symbol:
        return True
    return False


def gameLoop():
    playerList = gameInit()
    baseBoard = listInitalizer()
    turn = 1
    playing = True

    while playing:
        turn = turn % 2
        baseBoard = playerTurn(playerList[turn-1], baseBoard)
        boardPrint(baseBoard)
        if winCheck(baseBoard, playerList[turn-1]['symbol']):
            print(f'Congrats {playerList[turn-1]["name"]}, you won!')
            playerList = updateScore(playerList, playerList[turn-1]["name"])
            playing = False
        turn += 1


    baseBoard = playerTurn(playerList[0], baseBoard)
    boardPrint(baseBoard)
    baseBoard = playerTurn(playerList[1], baseBoard)
    boardPrint(baseBoard)

    return ''

gameLoop()
