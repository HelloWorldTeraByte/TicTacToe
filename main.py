def printBoard(board):
    print("\n")
    for i in range(3):
        print('|' + board[i *3] + '|' + board[i*3 + 1] + '|' + board[i*3+2] + '|')
        if(not i == 2):
            print("+-+-+-+")
    print("\n")
        
def updateBoard(board, position, symbol):
    return board.replace(position, symbol)

def PlayerSymbol(Player):
    if(Player == "X"):
        return "X"
    if(Player == "O"):
        return "O"
 
# return values
#      0:Tied
#      1:Player1 won
#      2:Player2 won
def HasWon(board, playerOneSymbol, playerTwoSymbol):
    if(len(usedPosition) == 9):
        return 0
    if(board[0] == playerOneSymbol and board[1] == playerOneSymbol and board[2] == playerOneSymbol):
        return 1
    if(board[3] == playerOneSymbol and board[4] == playerOneSymbol and board[5] == playerOneSymbol):
        return 1
    if(board[6] == playerOneSymbol and board[7] == playerOneSymbol and board[8] == playerOneSymbol):
        return 1
    if(board[2] == playerOneSymbol and board[4] == playerOneSymbol and board[6] == playerOneSymbol):
        return 1
    if(board[0] == playerOneSymbol and board[4] == playerOneSymbol and board[8] == playerOneSymbol):
        return 1
    
    if(board[0] == playerOneSymbol and board[3] == playerOneSymbol and board[6] == playerOneSymbol):
        return 1
    if(board[1] == playerOneSymbol and board[4] == playerOneSymbol and board[7] == playerOneSymbol):
        return 1
    if(board[2] == playerOneSymbol and board[5] == playerOneSymbol and board[8] == playerOneSymbol):
        return 1
       
        
    if(board[3] == playerTwoSymbol and board[4] == playerTwoSymbol and board[5] == playerTwoSymbol):
        return 2
    if(board[6] == playerTwoSymbol and board[7] == playerTwoSymbol and board[8] == playerTwoSymbol):
        return 2
    if(board[2] == playerTwoSymbol and board[4] == playerTwoSymbol and board[6] == playerTwoSymbol):
        return 2
    if(board[0] == playerTwoSymbol and board[4] == playerTwoSymbol and board[8] == playerTwoSymbol):
        return 2  
    
    if(board[0] == playerTwoSymbol and board[3] == playerTwoSymbol and board[6] == playerTwoSymbol):
        return 2
    if(board[1] == playerTwoSymbol and board[4] == playerTwoSymbol and board[7] == playerTwoSymbol):
        return 2
    if(board[2] == playerTwoSymbol and board[5] == playerTwoSymbol and board[8] == playerTwoSymbol):
        return 2    
    
board = "123456789"
usedPosition = []
playerOneSymbol = "A"
playerTwoSymbol = "A"

while(1):
    if(not (playerOneSymbol == "X" or playerOneSymbol == "O")):
        playerOneSymbol = str(input("Player one chose a symbol X O: "))
        playerOneSymbol = playerOneSymbol.upper()
        
    else:
        break
if(playerOneSymbol == "X"):
    playerTwoSymbol = "O"
if(playerOneSymbol == "O"):
    playerTwoSymbol = "X"

printBoard(board)
ShouldContinue = True

while(ShouldContinue): 
    
    if(ShouldContinue):   
        while(1):
            currentPosition = int(input("Player1: where do u want to go?: "))
            if (currentPosition in usedPosition) or (not(currentPosition < 10 and currentPosition > 0)):
                print("Sorry not valid!")
                
            else:
                usedPosition.append(currentPosition)
                board = updateBoard(board, str(currentPosition), "X")
                printBoard(board)
                if(HasWon(board, playerOneSymbol, playerTwoSymbol) == 1):
                    print("Player1 Won")
                    ShouldContinue = False
                if(HasWon(board, playerOneSymbol, playerTwoSymbol) == 0):
                    print("Tie!") 
                    ShouldContinue = False
                break
            
    if(ShouldContinue):  
        while(1):        
            currentPosition = int(input("Player2: where do u want to go?: "))
            if (currentPosition in usedPosition) or (not(currentPosition < 10 and currentPosition > 0)):
                print("Sorry not valid!")
                
            else:
                usedPosition.append(currentPosition)
                board = updateBoard(board, str(currentPosition), "O")
                printBoard(board)
                if(HasWon(board, playerOneSymbol, playerTwoSymbol) == 2):
                    print("Player2 Won")
                    ShouldContinue = False
                if(HasWon(board, playerOneSymbol, playerTwoSymbol) == 0):
                    print("Tie!")  
                    ShouldContinue = False
                break
