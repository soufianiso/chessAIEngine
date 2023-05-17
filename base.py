import numpy as np 
import pandas as pd 
from lib.board import Board, InitialState, PieceMovement

board = Board()
intialstate = InitialState()
movement = PieceMovement()
def main():
    set, count = intialstate.setpieces(board)
    movement.move(8, 'h', 5, 'h', board, 'R')
    print(board.state)
if __name__ == '__main__':
    main()





















