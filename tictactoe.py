import minimax
import state
import visual

test = True
aiTurn = True
gameboard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
initialState = minimax.State(gameboard)
actualState = minimax.State(gameboard[:])
print(actualState)
game = minimax.MiniMax()

validMoves = ['1', '2', '3', '4', '5', '6', '7', '8']

while(test):
  visual.visualize()
  if (aiTurn):
    testState = minimax.State(actualState.grid[:])
    # print(testState)
    move = game.MiniMaxDecision(testState)[1]
    actualState.TakeTurn(move, 'X')
    aiTurn = False
    print(actualState)
    print("AI took turn.")
  else:
    while(move not in validMoves and actualState.grid[int(move)] is not '-'):
      move = input()
    actualState.TakeTurn(int(move), 'O')
    aiTurn = True
    print(actualState)
    print("Player took turn.")
    
    