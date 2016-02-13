#Name: Anton Strickland

import minimax
import state
import visual

tryAgain = True
playing = True
aiTurn = True
gameboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
validMoves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
actualState = minimax.State(gameboard[:])
game = minimax.MiniMax()
remainingMoves = validMoves[:]
  
while(tryAgain):
  while(playing):
    visual.visualize(actualState.grid)
    if (aiTurn):
      print("AI's Move:")
      testState = minimax.State(actualState.grid[:])
      # print(testState)
      move = game.MiniMaxDecision(testState)
      actualState.TakeTurn(move, 'X')
      remainingMoves.remove(move)
      aiTurn = False
      print(actualState)
   
    else:
      print("Player's Move:")
      while(move not in remainingMoves and actualState.grid[int(move)-1] is not '-'):
        move = input()
      actualState.TakeTurn(int(move), 'O')
      remainingMoves.remove(move)
      aiTurn = True
      print(actualState)
      
    visual.visualize(actualState.grid)
    if (game.GoalTest(actualState, 'O')):
      playing = False
      print("You win!")
    elif (game.GoalTest(actualState, 'X')):
      playing = False
      print("AI wins!")
    elif (len(remainingMoves) == 0):
      playing = False
      print("Draw!")
  print("Play again? Y/N")
  p = input()
  if (p == "Y" or p == "y"):
    tryAgain = True
    playing = True
    aiTurn = True
    gameboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    validMoves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    actualState = minimax.State(gameboard[:])
    game = minimax.MiniMax()
    remainingMoves = validMoves[:]
  elif (p == "N" or p == "n"):
    tryAgain = False
    