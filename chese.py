def chess_board(board):
    # マス目がただしいか
    alpha = ['a','b','c','d','e','f','g','h']
    for mas in board.keys():
        if int(mas[0]) < 1 or int(mas[0]) > 8:
            return False
        if mas[1] not in alpha:
            return False

    # 駒がただしいか
    koma = ['pawn','knight','bishop','rook','queen','king']
    for km in board.values():
        if km[0] not in ['b','w']:
            return False
        if km[1:] not in koma:
            return False

    print('ただしいボード')
    return True

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h':'bqueen', '3e':'wking'}
chess_board(board)
