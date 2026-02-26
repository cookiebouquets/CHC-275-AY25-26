#tictactoe.py
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|",end = "")
            print(board[i][j], end = "|")
        print() #prints \n
    

def placePiece(board,current_player,row,col):  
    try:
        if board[row][col] == 0:
            board[row][col] = current_player #it replaces the (x,y) coordinate inside our board with the current_player's marker
            #there is a problem with our current implementation: We don't check if the (x,y) coordinate is an open square
            return True
        else:
            print("That is not a valid square")
            return False
    except Exception as e:
        print("That is not a valid square")
        return False
def switchPlayer(current_player):
    if current_player == "O":
        #this is the swap
        return "X"
    elif current_player == "X":
        return "O"
     
def checkWinner(board,current_player):
    #Row Victories
    for i in range(len(board)): #gets all of the rows
        if board[i][0] == current_player and board[i][1] == current_player and board[i][2] == current_player:
            print(f"{current_player} wins!")
            return True
    
    
    #Column Victories
    for j in range(len(board[0])):
        if board[0][j] == current_player and board[1][j] == current_player and board[2][j] == current_player:
            print(f"{current_player} wins!")
            return True
    
    
    #Diagonal Victories

    #Left Diagonal First
    if board[0][0] == board[1][1] == board[2][2] == current_player:
        print(f"{current_player} wins!")
        return True #when we want to exit the while loop of the actual game, we need some sort of flag variable 
    
    #Right Diagonal
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        print(f"{current_player} wins!")
        return True #when we want to exit the while loop of the actual game, we need some sort of flag variable         
    
    for row in board:
        for space in row:
            if space == 0:
                return False #the return statement not only flags the interpreter to remember a value, they also do one other thing
                #return also terminates the function call 
    print("It's a tie")
    return True

def main():
    grid = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    
    curr = "X"
    """ 
    How this shortcut works is:
    
    1) check winner is going to be evaluated
        a) if Check Winner evaluates to False, then we get False == False and the body of the while loop is going to execute
        b) if check winner evaluates to true, then  we get True == False so the body of the while loop is NOT going to execute
        
    2)This changes out first line of code in our while loop to be switchplayer, giving us "O" as the first player
    """
    while checkWinner(grid,curr) == False:
        printBoard(grid)
        curr = switchPlayer(curr)
        #now we want to ask for a row and a column to place the piece, but we don't want the current player to lose their
        #turn if they place a piece in a bad spot
        check = False
        while check == False:
            row = int(input(f"{curr}, Enter the Row: ").strip())
            col = int(input(f"{curr}, Enter the Col: ").strip())
            if placePiece(grid,curr,row,col) == True: #This is basically the same shortcut as the while loop, the body
                #of the if statement only executes if placePiece evaluates to true
                check = True
        

if __name__ == "__main__":
    main()
    
    
""" 
I set the current player to X initially for this reason: We know we want a while loop, 

while loop:
    1) Switch Player
    2) Place a Piece
    3) Check for the winner 
    
We can reformat this loop because of a python shortcut

Check winner returns either True or False. We also know that while loops exit on a conditional. We can make 
check winner effectively our conditional, and save a bunch of lines of code because we don't to create a bunch of check variables
and do a bunch of variable assignments 


"""