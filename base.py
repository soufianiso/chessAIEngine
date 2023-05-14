import numpy as np 
import pandas as pd 
from board import Board

W = 8
H = 8
disp = Board(H,W)
bb = disp.draw()
piece1 = 'R'
piece2 = 'P'
disp.move(piece1,1,'a')
disp.move(piece2,1,'e')
disp.move(piece2,1,'h')
print(bb)






















