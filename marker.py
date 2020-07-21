def player_input():
    marker = ''

    while marker != 'X' and marker !='O':
        marker = input ('player1: choose X or O : ').upper()

        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X'
