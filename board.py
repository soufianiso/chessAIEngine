import numpy as np
import pandas as pd

Pieces = ('R','N','B','K','Q','B','N','R','P')
class Board:
    def __init__(self, cols, rows):
        self._cols = 8
        self._rows = 8
        self._pieces = list(Pieces)
        self._board = None

    def draw(self):
        df = np.full((self._cols,self._rows),'.').astype(str)
        self._board = pd.DataFrame(df, index = [1,2,3,4,5,6,7,8], columns=['a','b','c','d','e','f','g','h'] )

        # setting _pieces rows by label locations
        self._board.loc[1] = [self._pieces[i] for i in range(len(self._pieces)-1)] 
        self._board.loc[8] = [self._pieces[i] for i in range(len(self._pieces)-1)] 
        self._board.loc[2] = [self._pieces[-1] for i in range(len(self._pieces)-1)] 
        self._board.loc[7] = [self._pieces[-1] for i in range(len(self._pieces)-1)]
        return self._board


    def move(self, piece, row, col):
        if piece in self._pieces:
            self._board.loc[row,col] = '.' 
            return self._board

