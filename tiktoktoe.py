def display_game(board):
    print("    |   |  ")
    print("  "+board[0]+" | "+board[1]+" | "+board[2])
    print("    |   |  ")
    print("-------------")
    print("    |   |  ")
    print("  "+board[3]+" | "+board[4]+" | "+board[5])
    print("    |   |  ")
    print("-------------")
    print("    |   |  ")
    print("  "+board[6]+" | "+board[7]+" | "+board[8])
    print("    |   |  ") 

def input_user():
    player1 = 'Z'
    while player1 not in ['X','O']:
        player1 = input("Player1, What do you want to take : X or O :- ")
        if player1 not in ['X','O']:
            print("Invalid Entry!")
    return player1

def choose_position():
    board = [" "]*9
    p1_position = "100"
    while p1_position not in ["0","1","2","3","4","5","6","7","8","9"]:
        p1_position = input("Player 1 choose a position : ")

    return p1_position

def choose_position2():
    board = [" "]*9
    p2_position = "100"
    while p2_position not in ["0","1","2","3","4","5","6","7","8","9"]:
        p2_position = input("Player 2 choose a position : ")

    return p2_position

def game_on():
    gameon = 'Z'
    while gameon not in ['Y','N']:
        gameon = input("Do you want to play more??: (Y or N) ")
        if gameon not in ['Y','N']:
            print("Invalid Entry!")
    return gameon
 
def game_winner(board):
    if board[0] == board[1] == board[2]  == "X":
        return("Player 1 won.")
    elif board[3] == board[4] == board[5]  == "X":
        return("Player 1 won.")
    elif board[6] == board[7] == board[8]  == "X":
        return("Player 1 won.")
    elif board[0] == board[4] == board[8]  == "X":
        return("Player 1 won.")
    elif board[2] == board[4] == board[6]  == "X":
        return("Player 1 won.")
    elif board[0] == board[3] == board[6]  == "X":
        return("Player 1 won.")
    elif board[1] == board[4] == board[7]  == "X":
        return("Player 1 won.")
    elif board[2] == board[5] == board[8]  == "X":
        return("Player 1 won.")
    if board[0] == board[1] == board[2]  == "O":
        return("Player 2 won.")
    elif board[3] == board[4] == board[5]  == "O":
        return("Player 2 won.")
    elif board[6] == board[7] == board[8]  == "O":
        return("Player 2 won.")
    elif board[0] == board[4] == board[8]  == "O":
        return("Player 2 won.")
    elif board[2] == board[4] == board[6]  == "O":
        return("Player 2 won.")
    elif board[0] == board[3] == board[6]  == "O":
        return("Player 2 won.")
    elif board[1] == board[4] == board[7]  == "O":
        return("Player 2 won.")
    elif board[2] == board[5] == board[8]  == "O":
        return("Player 2 won.")
 
def update_display(board):
    display_game(board)
    gameon = 'Y'
    p1_player = input_user()
    if (p1_player == "X"):
        p2_player = 'O'
    else:
        p2_player = 'X'
        
        
    while gameon == 'Y' or playmore == 'Y':
        p1_position = int(choose_position())
        board[p1_position] = p1_player
        new_game = display_game(board)
        p1 = game_winner(board)
        print(p1)
        if (p1 == "Player 1 won." or p1 == 'Player 2 won.'):
            break       
        p2_position = int(choose_position2())
        board[p2_position] = p2_player
        new_game = display_game(board)
        game_winner(board)
        p1 = game_winner(board)
        print(p1)
        if (p1 == "Player 1 won." or p1 == 'Player 2 won.'):
            break
            
        
        gameon = game_on()
    if (p1 == "Player 1 won." or p1 == 'Player 2 won.'):
        playmore = input("Do you want to play one more game? (Y or N)")
        if playmore == 'Y':
            update_display([" "]*9)
            
        
    return new_game 


update_display([" "]*9)

