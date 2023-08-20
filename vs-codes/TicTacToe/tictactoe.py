# 1.) Creating global variables:
import random

# a.) Create the board piece, as a list. A 3 * 3 square of dashes.
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# b.) We'll start every game with a player, initialized by string x.
currentPlayer = "x"

# c.)Winner variable originally initialized with no value.
winner = None

# d.) Controls the loop that controls who'll win or tie.
gameRunning = True

#2.) Printing the game board.
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
#printBoard(board) 

#3.) Take player input.
def playerInput(board):
    inp = int(input("Enter a number 1 - 9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already in that spot!")
        switchPlayer()

#4.) Check for win or tie. You can win: horizontally, up & down or diagonally.
#a.) Check for win.
def checkHorizontal(board):
    global winner
    #Global keyword means that if we make changes to the winner variable within the scope of the function,
    #The winner variable changes within the scope of the entire file.
    
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0] #or board[1] or board[2], cause they're all equal.
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif  board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
#b.)Check for tie.
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

#We create one last master function, so that we don't have to type all these into the gameRunning variable.
#This is where we use the return True statement we used earlier.
def checkWin(board):
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False 
        exit()
    
#5.) Switch the player.
def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"

#Computer       
#Create an ability for the comp to make some moves, so we don't go against ourselves.
def computer(board):
    #create a loop for whenever the comp is up to make a move.
    while currentPlayer == "o":
        #We'll tap into that random module & generate a random no: 0-8
          position = random.randint(0, 8)
          #Check if that position on the board is occupied.
          if board[position] == "-":
              board[position] = "o"
              switchPlayer()

#6.) Check for win or tie again.
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board) #After the comp's turn.
    checkTie(board)
    
