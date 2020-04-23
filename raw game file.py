from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7]+ ' | ' +board[8]+ ' | ' +board[9])
    print('   |   |')
    print('--------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('--------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')






    test_board = ['#', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o' ,'x']
    dislay_board(test_board)
    display_board(test_board)
    display_board(test_board)

    def player_input():
    marker = ''

    while marker != 'X' and marker !='O':
        marker = input ('player1: choose X or O : ').upper()

        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')


    player1_marker ,player2_marker = player_input()

    player1_marker

    def place_marker(board,marker, position):

    board[position] = marker


    test_board

    place_marker(test_board, '$', 8 )
    display_board(test_board)





def win_check(board, mark)
    # WIN TIC TAC TOE ?
    return ((board [7] == mark and board[8] == mark and board[9] == mark) or #across the middle
    (board [4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board [1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board [7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board [8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board [9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board [7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board [9] == mark and board[5] == mark and board[1] == mark)) # diagonal


    # ALL COLUMNS, check to see if marker matches
    # 2 diagonals , check for matching



    display_board(test_board)
    win_check(test_board, 'X')


    import random

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board, position):
    return board[position] == ' '

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

def replay():

    choice = input("Play again? Enter Yes or No")

    return choice == 'YES'

# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to TIC TAC TOE')

while True:

    #play the game

    ## SET EVERYTHING UP(BOARD, WHOS FIRST, CHOOSE MAKERS X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + 'will go first')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # game play

    while game_on:
        if turn == 'player1':

            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)

            # place the marker on the position
            place_marker(the_board,player1_marker,position)

            #chcek if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'player 2'


        else:
             # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)

            # place the marker on the position
            place_marker(the_board,player2_marker,position)

            #chcek if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'player1'


    if not replay():
        break
