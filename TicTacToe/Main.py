board=['-','-','-',
       '-','-','-',
       '-','-','-',]
game_is_going=True
def dispay_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3] +'|'+board[4]+'|'+board[5])
    print(board[6] +'|'+board[7]+'|'+board[8])

def play_game():

    dispay_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    handle_turn()
def handle_turn():
    position=input('choose a position between 1-9:')
    position=int(position)-1
    board[position]='X'
    dispay_board()
play_game()
def check_if_game_over():
    check_if_win()
    check_if_tie()
def check_if_win():
    return

def check_if_tie():
    return

def flip_player():
    return