def win_check(board, mark):
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
