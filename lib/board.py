import numpy as np
import pandas as pd

# Pieces
pieces = ('R','N','B','K','Q','B','N','R','P')

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
        total = 0
        for i in self._pieces:
            total += 1 
        return f"total of pieces remaining {total}"

   
class InitialState:

    # placing the pieces to begin to play
    def setpieces(self, board: Board):
        pieces = Piece().pieces
        count = Piece().count
        state = board.state 
        counting = len(pieces) - 1
        state.loc[1] = [pieces[i] for i in range(counting)] 
        state.loc[8] = [pieces[i] for i in range(counting)] 
        state.loc[2] = [pieces[-1] for i in range(counting)] 
        state.loc[7] = [pieces[-1] for i in range(counting)]
        
        return state, count


class PieceMovement:
    
    pass


class Player:
    def __init__(self):
        self.score: int = 0






































    # def draw(self):
    #     df = np.full((self._cols,self._rows),'.').astype(str)
    #     self._board = pd.DataFrame(df, index = [1,2,3,4,5,6,7,8], columns=['a','b','c','d','e','f','g','h'] )

    #     # setting _pieces rows by label locations
    #     self._board.loc[1] = [self._pieces[i] for i in range(len(self._pieces)-1)] 
    #     self._board.loc[8] = [self._pieces[i] for i in range(len(self._pieces)-1)] 
    #     self._board.loc[2] = [self._pieces[-1] for i in range(len(self._pieces)-1)] 
    #     self._board.loc[7] = [self._pieces[-1] for i in range(len(self._pieces)-1)]
    #     return self._board


    # def move(self, piece, row, col):
    #     if piece in self._pieces:
    #         self._board.loc[row,col] = '.' 
    #         return self._board

