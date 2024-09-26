"""
Connor Cox
U2 L3
Tic Tac Toe
"""
import os
from random import choice
from tic_tac_toe import TicTacToe
from time import sleep

Game = TicTacToe()

def player_check():
  good = False
  while not(good):
    placement = input("Where would you like to place your token? (Ex. a3) ")
    place = list(placement)
    lets = ['a', 'b', 'c']
    nums = ['1', '2', '3']
    if place[0] in lets and place[1] in nums and not(Game.taken(placement)):
      good = True
      break
    print("WRONG! Try again.\n")
  return placement

def computer_turn():
  lets = ['a', 'b', 'c']
  nums = ['1', '2', '3']
  good = False
  while not(good):
    placement = choice(lets) + choice(nums)
    if not(Game.taken(placement)):
      good = True
  win = Game.place_token(placement)
  return win

def player_turn():
  placement = player_check()
  win = Game.place_token(placement)
  return win

def main():
  win = False
  print(Game)
  while not(win):
    win = player_turn()
    os.system('clear')
    print(Game)
    if win:
      break
    sleep(3)
    os.system('clear')
    win = computer_turn()
    print(Game)
  """
  win = Game.place_token("a3")
  win = Game.place_token("a2")
  win = Game.place_token("a1")
  print(Game)
  """
  print(Game.is_winner())


if __name__ == "__main__":
  main()