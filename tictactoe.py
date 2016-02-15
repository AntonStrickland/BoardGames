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
Vis = visual.Visualizer()
  
while(tryAgain):

  while(playing):
    Vis.visualize(actualState,0,100)
    if (actualState.aiTurn):
      print("AI's Move:")
      testState = minimax.State(actualState.grid[:])
      # print(testState)
      move = game.MiniMaxDecision(testState)
      actualState.TakeTurn(move)
      remainingMoves.remove(move)
    else:
      print("Player's Move:")
      while(move not in remainingMoves):
        move = Vis.getInput()
      actualState.TakeTurn(int(move))
      remainingMoves.remove(move)
      
    Vis.visualize(actualState,0,100)
    if (game.GoalTest(actualState, 'O')):
      playing = False
      print("You win!")
      print("Play again? Y/N")
    elif (game.GoalTest(actualState, 'X')):
      playing = False
      print("AI wins!")
      print("Play again? Y/N")
    elif (len(remainingMoves) == 0):
      playing = False
      print("Draw!")
      print("Play again? Y/N")

  p = Vis.checkNextGame()
  if (p == 'Y'):
    tryAgain = True
    playing = True
    aiTurn = True
    gameboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    validMoves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    actualState = minimax.State(gameboard[:])
    game = minimax.MiniMax()
    remainingMoves = validMoves[:]
  elif (p == 'N'):
    tryAgain = False
    