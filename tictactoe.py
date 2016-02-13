#Name: Anton Strickland

import minimax
import state
import visual

test = True
aiTurn = True
gameboard = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
initialState = minimax.State(gameboard)
actualState = minimax.State(gameboard[:])
print(actualState)
game = minimax.MiniMax()

validMoves = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
remainingMoves = validMoves[:]
print (remainingMoves)

while(test):
  visual.visualize()
  if (aiTurn):
    testState = minimax.State(actualState.grid[:])
    # print(testState)
    move = game.MiniMaxDecision(testState)
    actualState.TakeTurn(move, 'X')
    remainingMoves.remove(move)
    aiTurn = False
    print(actualState)
    print("AI took turn.")
  else:
    while(move not in remainingMoves and actualState.grid[int(move)] is not '-'):
      move = input()
    actualState.TakeTurn(int(move), 'O')
    remainingMoves.remove(move)
    aiTurn = True
    print(actualState)
    print("Player took turn.")
  if (game.GoalTest(actualState, 'O')):
    test = False
    print("You win!")
  elif (game.GoalTest(actualState, 'X')):
    test = False
    print("AI wins!")
    
    