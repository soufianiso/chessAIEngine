import numpy as np 
import pandas as pd 
from lib.board import Board , InitialState


board = Board()
setpieces = InitialState()

def main():
    set, count = setpieces.setpieces(board)
    print(set)
    print(count)


if __name__ == '__main__':
    main()





















