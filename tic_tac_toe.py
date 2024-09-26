"""
Connor Cox
U2 L3
Tic Tac Toe
"""
from random import choice

class TicTacToe:

  def __init__(self):
    self.__board = [[" ", " ", " "] for i in range(3)]
    self.__turn = "X"

  def __str__(self):
    out = (f"""
     |   |
3  {self.__board[0][0]} | {self.__board[0][1]} | {self.__board[0][2]} 
  ___|___|___
     |   |   
2  {self.__board[1][0]} | {self.__board[1][1]} | {self.__board[1][2]} 
  ___|___|___
     |   |   
1  {self.__board[2][0]} | {self.__board[2][1]} | {self.__board[2][2]}
     |   |
   a   b   c
    """)

    return out
  
  def __check_win(self):
    win = False
    nums = ['3', '2', '1']
    for i in range(3):
      matchesH = 0
      matchesDR = 0
      matchesDL = 0
      matchesV = 0
      for j in range(3):
        if self.__board[i][j] == self.__turn:
          matchesH +=1
        if self.__board[j][j] == self.__turn:
          matchesDR += 1
        if self.__board[2-j][j] == self.__turn:
          matchesDL += 1
        if self.__board[j][i] == self.__turn:
          matchesV += 1

        if matchesH == 3 or matchesDL == 3 or matchesDR == 3 or matchesV == 3:
          win = True
    return win
  
  def is_winner(self):
    print(self.__turn)
    out = (f"Player {self.__turn} Wins!")
    
    return out
  
  def place_token(self, placement):
    spot = list(placement)
    lets = ['a', 'b', 'c']
    nums = ['3', '2', '1']
    y = lets.index(spot[0])
    x = nums.index(spot[1])
    self.__board[x][y] = self.__turn

    win = self.__check_win()

    if win == False:
      if self.__turn == "X":
        self.__turn = "O"
      else:
        self.__turn = "X"
    
    return win
  
  def taken(self, placement):
    spot = list(placement)
    lets = ['a', 'b', 'c']
    nums = ['3', '2', '1']
    y = lets.index(spot[0])
    x = nums.index(spot[1])
    bad = False

    if self.__board[x][y] == "X" or self.__board[x][y] == "O":
      bad = True
    
    return bad
    


 