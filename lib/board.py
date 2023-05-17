import numpy as np
import pandas as pd

# Pieces
pieces = ('R','N','B','K','Q','B','N','R','P','P','P','P','P','P','P','P')

class Board:
    # drawing the baord
    def __init__(self):
        self._cols: int = 8
        self._rows: int = 8
        self._df: str = np.full((self._cols,self._rows),'.').astype(str)
        self._board: object = pd.DataFrame(self._df, index = [1,2,3,4,5,6,7,8], columns=['a','b','c','d','e','f','g','h'] )

    @property
    def state(self) -> object:
        return self._board


class Piece:
    def __init__(self):
        self._pieces = list(pieces) 

    # return list of pices 
    @property
    def pieces(self) -> list:
        return self._pieces

    # return how many pieces in one set
    @property
    def count(self) -> int:
        return len(self._pieces)

   
class InitialState:

    # placing the pieces to begin to play
    def setpieces(self, board: Board):
        pieces = Piece().pieces
        count = Piece().count
        state = board.state 
        state.loc[1] = [pieces[i] for i in range(8)] 
        state.loc[8] = [pieces[i] for i in range(8)] 
        state.loc[2] = [pieces[-1] for i in range(8)] 
        state.loc[7] = [pieces[-1] for i in range(8)]
        return state, count


class PieceMovement:
    def move(self,initrow,initcol, row, col, board: Board, piece):
        state = board.state
        # Rook
        if piece == 'R':
            if initrow == row or initcol == col:
                state.loc[row,col] = piece 
                return state.loc[row,col] 
        # Knight
        if piece == 'N':
            pass

        # Bishop
        if piece == 'B':
            pass

        # Queen
        if piece == 'Q':
            pass

        # King
        if piece == 'K':
            pass

        # Pawn
        if piece == 'P':
            pass













