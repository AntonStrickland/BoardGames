#Name: Anton Strickland

import minimax
import state
#import visual

test = True
aiTurn = True
gameboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
initialState = minimax.State(gameboard)
actualState = minimax.State(gameboard[:])
print(actualState)
game = minimax.MiniMax()

validMoves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
remainingMoves = validMoves[:]
print (remainingMoves)

while(test):
  # visual.visualize()
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
    
    
  if (game.GoalTest(actualState, 'O')):
    test = False
    print("You win!")
  elif (game.GoalTest(actualState, 'X')):
    test = False
    print("AI wins!")
  elif (len(remainingMoves) == 0):
    test = False
    print("Draw!")
        
    
    