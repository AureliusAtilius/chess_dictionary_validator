

def isValidChessBoard(board):
    black_pieces={"bpawn": 0, "brook":0,"bbishop":0,"bknight":0,"bqueen":0,"bking":0}
    white_pieces={"wpawn": 0, "wrook":0,"wbishop":0,"wknight":0,"wqueen":0,"wking":0}
    for i in board.values():
        if i[0]=="b":
            for x in black_pieces:
                if i ==x:
                    black_pieces[x]+=1
        elif i[0]=="w":
            for x in white_pieces:
                if i ==x:
                    white_pieces[x]+=1

    valid_squares=[
        "a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8",
        "c1","c2","c3","c4","c5","c6","c7","c8","d1","d2","d3","d4","d5","d6","d7","d8",
        "e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8",
        "g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]
    board_valid=True
    if black_pieces["bpawn"]>8:
        board_valid=False
    if black_pieces["bking"]>1:
        board_valid=False
    if white_pieces["wpawn"]>8:
        board_valid=False
    if white_pieces["wking"]>1:
        board_valid=False
    if sum(black_pieces.values()) > 16:
        board_valid=False
    if sum(white_pieces.values()) > 16:
        board_valid=False
    for i in board.keys():
        if i not in valid_squares:
            board_valid=False


    return board_valid




test_board = {"h1":"bking","c6":"wqueen","g2":"bbishop","h5":"bqueen","e3":"wking"}
print(isValidChessBoard(test_board))