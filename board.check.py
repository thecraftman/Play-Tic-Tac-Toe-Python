def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
        #BOARD IS FULL IF WE RETURN TRUE
    return True


def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position:(1-9) '))

    return position
