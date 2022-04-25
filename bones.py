class Piece():
    def __init__(self, piecetype, side, alive=True):
        self.piecetype = piecetype
        self.side = side
        self.alive = alive

class Board():
    def __init__(self):
        background = [[0 for i in range(8)] for j in range(8)]
        toggle = True
        for i in range(8):
            if i%2 == 1:
                toggle = False
            else:
                toggle = True
            for j in range(8):
                if toggle:
                    toggle = False
                else:
                    background[i][j] = 1
                    toggle = True
        self.board = background
    def create_pieces(self):
        wRook1 = Piece("r","w")
        wRook2 = Piece("r", "w")
        wKnight1 = Piece("k", "w")
        wKnight2 = Piece("k", "w")
        wBishop1 = Piece("b", "w")
        wBishop2 = Piece("b", "w")
        wQueen = Piece("q", "w")
        wKing = Piece("k", "w")
        bRook1 = Piece("r","b")
        bRook2 = Piece("r", "b")
        bKnight1 = Piece("k", "b")
        bKnight2 = Piece("k", "b")
        bBishop1 = Piece("b", "b")
        bBishop2 = Piece("b", "b")
        bQueen = Piece("q", "b")
        bKing = Piece("k", "b")
        wPawn1 = Piece("p","w")
        wPawn2 = Piece("p","w")
        wPawn3 = Piece("p","w")
        wPawn4 = Piece("p","w")
        wPawn5 = Piece("p","w")
        wPawn6 = Piece("p","w")
        wPawn7 = Piece("p","w")
        wPawn8 = Piece("p","w")
        bPawn1 = Piece("p","b")
        bPawn2 = Piece("p","b")
        bPawn3 = Piece("p","b")
        bPawn4 = Piece("p","b")
        bPawn5 = Piece("p","b")
        bPawn6 = Piece("p","b")
        bPawn7 = Piece("p","b")
        bPawn8 = Piece("p","b")
    def set_board(self):
        board_state = [['' for i in range(8)] for i in range(8)]
        board_state[0][0] = bRook1
        board_state[0][1] = bKnight1
        board_state[0][2] = bBishop1
        board_state[0][3] = bQueen
        board_state[0][4] = bKing
        board_state[0][5] = bBishop1
        board_state[0][6] = bKnight1
        board_state[0][7] = bRook1
        board_state[7][0] = wRook1
        board_state[7][1] = wKnight1
        board_state[7][2] = wBishop1
        board_state[7][3] = wQueen
        board_state[7][4] = wKing
        board_state[7][5] = wBishop1
        board_state[7][6] = wKnight1
        board_state[7][7] = wRook1
        print(board_state)





newBoard = Board()
print(newBoard.board)
newBoard.create_pieces()
newBoard.set_board()
        