# version : python 3.9   
# desc    : delete duplication from a given list
# author  : Sahraoui Mohammed Taher Amine.
import random
def printBoard(board):
    for r in board:
        print(r)

def isNotOccupied(field):
    if field == " ":
        return True

def checkGameState(board, symbol, state):

    if symbol == "X":
        state[1]  = checkWinning(board, symbol)
        if state[1]:
            state[2] = False
            return state
    elif symbol == "O":
        state[0] = checkWinning(board, symbol)
        if state[0]:
            state[2] = False
            return state
        
    tie = True
    for r in board:
        for c in r:
            if isNotOccupied(c):
                tie = False
                break
    if tie:
        state[2] = False            
    return state   
    


def checkWinning(board,symbol):

    # check the rows
    counter = 0
    for r in board:
        for c in r:
            if c == symbol:
                counter += 1
        if counter == 3:
            return True
        counter = 0
        
    # check the columns
    for i in range(3):
        for j in range(3):
            if board[j][i] == symbol:
                counter += 1
        if counter == 3:
            return True
        counter = 0
    # check the diagonals
    for i in range(3):
        if board[i][i] == symbol:
            counter += 1
    if counter == 3:
        return True
    counter = 0

    for i in range(3):
        if board[i][2-i] == symbol:
            counter += 1
    if counter == 3:
        return True
    
    # if no condition is met, return false
    return False
    
    
def gameDecision(state):
    if not state[2]:
        if state[0]:
            print(" ----- user won -----")
        elif state[1]:
            print("----- computer won -----")
        else:
            print("----- tie -----")
        # game is over the continue state is false so game is false
        return False
    else:
        # game is not over, continue
        return True


# creating a tic tac toe game
board = [ [" ", " ", " "] for x in range(3) ]
indexies = [(0,0), (0,1), (0,2), 
            (1,0), (1,1), (1,2), 
            (2,0), (2, 1), (2,2)
           ]
state = [False, False, True]
choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game = True
init = True
while game:  
    user_turn = True
    computer_turn = False
    if init:
        print("starting the game:")
        printBoard(board)
        print("computer's turn:")
        computer = 5
        turn = indexies[computer - 1]
        board[turn[0]][turn[1]] = "X"
        printBoard(board)
        choice.remove(computer)
    init = False
    while user_turn:
        user = int(input("user's turn: "))
        if 1 <= user < 10:
            turn = indexies[user - 1]
            if  isNotOccupied(board[turn[0]][turn[1]]):
                board[turn[0]][turn[1]] = "O"
                user_turn = False
                computer_turn = True
                state = checkGameState(board, "O", state)
                printBoard(board)
                choice.remove(user)
            else:
                continue
        else:
            continue

    while computer_turn:
        print("computer's turn:")
        computer = choice[random.randint(0, len(choice) - 1)]
        turn = indexies[computer - 1]
        if  isNotOccupied(board[turn[0]][turn[1]]):
            board[turn[0]][turn[1]] = "X"
            computer_turn = False
            user_turn = True
            state = checkGameState(board, "X", state)
            printBoard(board)
            choice.remove(computer)
        else:
            continue
    game = gameDecision(state)
    #print(choice)
    #print(game)

    


#make the computer smarter, by not selecting a field that is already occupied;
