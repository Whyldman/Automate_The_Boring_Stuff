bad_board_1 = {'1a':'brook', '1b':'bknight','1c':'bbishop', '1d':'bqueen',
              '1e':'bking', '1f':'bbishop', '1g':'bknight','1h':'brook',
              '2a':'bpawn', '2b':'bpawn','2c':'bpawn', '2d':'bpawn',
              '2e':'bpawn', '2f':'bpawn', '2g':'bpawn','2h':'bpawn',
              '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn',
              '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
              '8a':'wrook', '8b':'wknight','8c':'wbishop', '8d':'wqueen',
              '8e':'bking', '8f':'wbishop', '8g':'wknight','8h':'wrook'}

bad_board_2 = {'1a':'brook', '1b':'bknight','1c':'bbishop', '1d':'bqueen',
              '1e':'bking', '1f':'bbishop', '1g':'bknight','1h':'brook',
              '2a':'bpawn', '2b':'bpawn','2c':'bpawn', '2d':'bpawn',
              '2e':'bpawn', '2f':'bpawn', '2g':'bpawn','2h':'bpawn',
              '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn',
              '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
              '8a':'wpawn', '8b':'wknight','8c':'wbishop', '8d':'wqueen',
              '8e':'wking', '8f':'wbishop', '8g':'wknight','8h':'wrook'}

bad_board_3 = {'1a':'brook', '1b':'bknight','1c':'bbishop', '1d':'bqueen',
              '1e':'bking', '1f':'bbishop', '1g':'bknight','1h':'brook',
              '2a':'bpawn', '2b':'bpawn','2c':'bpawn', '2d':'bpawn',
              '2e':'bpawn', '2f':'bpawn', '2g':'bpawn','2h':'bpawn',
              '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn',
              '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
              '8a':'wrook', '8b':'wknight','8c':'wbishop', '8d':'wqueen',
              '8e':'wking', '8f':'wbishop', '8g':'wknight','9h':'wrook'}

bad_board_4 = {'1a':'brook', '1b':'bknight','1c':'bbishop', '1d':'bqueen',
              '1e':'bking', '1f':'bbishop', '1g':'bknight','1h':'brook',
              '2a':'bpawn', '2b':'bpawn','2c':'bpawn', '2d':'bpawn',
              '2e':'bpawn', '2f':'bpawn', '2g':'bpawn','2h':'bpawn',
              '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn',
              '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
              '8a':'wrook', '8b':'wknight','8c':'wbishop', '8d':'wqueen',
              '8e':'wking', '8f':'wbishop', '8g':'wknight','8h':'wrook',
              '5a': 'wpawn'}

bad_board_5 = {'1a':'brook', '1b':'bknight','1c':'bbishop', '1d':'bqueen',
              '1e':'bking', '1f':'bbishop', '1g':'bknight','1h':'brook',
              '2a':'bpawn', '2b':'bpawn','2c':'bpawn', '2d':'bpawn',
              '2e':'bpawn', '2f':'bpawn', '2g':'bpawn','2h':'bpawn',
              '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn',
              '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
              '8a':'wrook', '8b':'wknight','8c':'wbishop', '8d':'wqueen',
              '8e':'wking', '8f':'wbishop', '8g':'wknight','8h':'crook'}

bad_board_6 = {'1a':'brook', '1b':'bknight','1c':'bbishop', '1d':'bqueen',
              '1e':'bking', '1f':'bbishop', '1g':'bknight','1h':'brook',
              '2a':'bpawn', '2b':'bpawn','2c':'bpawn', '2d':'bpawn',
              '2e':'bpawn', '2f':'bpawn', '2g':'bpawn','2h':'bpawn',
              '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn',
              '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
              '8a':'wrook', '8b':'wknight','8c':'wbishop', '8d':'wqueen',
              '8e':'wking', '8f':'wbishop', '8g':'wknight','8h':'wbook'}

good_board = {'1a':'brook', '1b':'bknight','1c':'bbishop', '1d':'bqueen',
              '1e':'bking', '1f':'bbishop', '1g':'bknight','1h':'brook',
              '2a':'bpawn', '2b':'bpawn','2c':'bpawn', '2d':'bpawn',
              '2e':'bpawn', '2f':'bpawn', '2g':'bpawn','2h':'bpawn',
              '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn',
              '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
              '8a':'wrook', '8b':'wknight','8c':'wbishop', '8d':'wqueen',
              '8e':'wking', '8f':'wbishop', '8g':'wknight','8h':'wrook'}

import pprint
def countPieces(board):
    count = {}
    pieces = {}

    for v in board.values():

        if v[0] not in ['w', 'b']:
            print('Non Black or White Piece. You have a piece starting with ' + v[0])
        elif v[1:] not in ['pawn', 'rook', 'knight', 'bishop', 'king', 'queen']:
            print('Not a pawn, rook, knight, bishop, king, or queen. You have a piece called ' + v[1:])

        piece = v[0]
        count.setdefault(piece, 0)
        count[piece] = count[piece] + 1

        pieces.setdefault(v, 0)
        pieces[v] = pieces[v] + 1

    if pieces.get('wpawn', 0) > 8:
        print('Too many white pawns')
    elif pieces.get('bpawn', 0) > 8:
        print('Too many black pawns')
    elif pieces.get('wrook', 0) > 2:
        print('Too many white rooks')
    elif pieces.get('brook', 0) > 2:
        print('Too many black rooks')
    elif pieces.get('wknight', 0) > 2:
        print('Too many white knights')
    elif pieces.get('bknight', 0) > 2:
        print('Too many black knights')
    elif pieces.get('wbishop', 0) > 2:
        print('Too many white bishops')
    elif pieces.get('bbishop', 0) > 2:
        print('Too many black bishops')
    elif pieces.get('wqueen', 0) > 1:
        print('Too many white queens')
    elif pieces.get('bqueen', 0) > 1:
        print('Too many black queens')
    elif pieces.get('wking', 0) > 1:
        print('Too many white kings')
    elif pieces.get('bking', 0) > 1:
        print('Too many black kings')
    else:
        print('Pieces look right!')

    return pprint.pprint(pieces)

def boardBoundary(board):

    for k in board.keys():

        if int(k[0]) > 8 or int(k[0]) < 0:
            print('Not a valid row. You have a piece on row ' + k[0] \
                    + '. Pieces must be between rows 1 and 8')

        if k[1] > 'h' or k[1] < 'a':
            print('Not a valid column. You have a piece on column ' + k[1] \
                + '. Pieces must be between columns a and h')

    return print("Pieces are on the board.")

def isGoodBoard(board):

    boardBoundary(board)
    countPieces(board)

print(isGoodBoard(good_board))

print(isGoodBoard(bad_board_1))
print(isGoodBoard(bad_board_2))
print(isGoodBoard(bad_board_3))
print(isGoodBoard(bad_board_4))
print(isGoodBoard(bad_board_5))
print(isGoodBoard(bad_board_6))
