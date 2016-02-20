def printBoard(board):
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    if board['top-L'] == player:
        if board['mid-L'] == player:
            if board['low-L'] == player:
                return True
    elif board['top-M'] == player:
        if board['mid-M'] == player:
            if board['low-M'] == player:
                return True
    elif board['top-R'] == player:
        if board['mid-R'] == player:
            if board['low-R'] == player:
                return True
    elif board['top-L'] == player:
        if board['top-M'] == player:
            if board['top-R'] == player:
                return True
    elif board['mid-L'] == player:
        if board['mid-M'] == player:
            if board['mid-R'] == player:
                return True
    elif board['low-L'] == player:
        if board['low-M'] == player:
            if board['low-R'] == player:
                return True
    elif board['top-L'] == player:
        if board['mid-M'] == player:
            if board['low-R'] == player:
                return True
    elif board['top-R'] == player:
        if board['mid-M'] == player:
            if board['low-L'] == player:
                return True
    else:
        return False
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
       
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer #Lets the starting player (X or O) start.
    for i in range(9): #Allows for 9 turns, as there are 9 spots on the board.
        printBoard(board) #Prints the board.
        print('Turn for ' + turn + '. Move on which space?') #Tells which player is to take his/her turn next.
        move = input() #Takes the input of the player's move.
        board[move] = turn 
        if( checkWinner(board, 'X') ): #Checks if X wins,
            print('X wins!') #And prints if it does
            break #Breaks the loop
        elif ( checkWinner(board, 'O') ): #Checks if O wins,
            print('O wins!') #And prints if it does
            break #Breaks the loop
    
        if turn == 'X': 
            turn = 'O'
        else:
            turn = 'X' #The above 3 lines switches between X and O's turn
        
    printBoard(board) #Prints the board
