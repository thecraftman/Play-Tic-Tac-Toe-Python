# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to TIC TAC TOE')

while True:

    #play the game

    ## SET EVERYTHING UP(BOARD, WHOS FIRST, CHOOSE MAKERS X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first(
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
