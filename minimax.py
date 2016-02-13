import sys

class State():
  def __init__(self, grid):
    self.grid = grid
    
  def TakeTurn(self, action, letter):
    self.grid[int(action)-1] = letter
    return
    
  def __str__(self):
    return self.grid[0] + self.grid[1] + self.grid[2] + "\n" + self.grid[3] + self.grid[4] + self.grid[5] + "\n" + self.grid[6] + self.grid[7] + self.grid[8] + "\n"
    
class MiniMax():
  def __init__(self):
    self.actionSet = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    self.myLetter = 'X'
    self.urLetter = 'O'
    self.finalAction = None

  def MiniMaxDecision(self, initialState):
    # print(initialState.grid)
    v = self.MinValue(initialState)
    return self.finalAction
    
  def MinValue(self, state):
    if (self.TerminalTest(state)):
      return self.Utility(state)
    v = 99
    for action in self.actionSet:
      # Only make valid actions
      if (self.CheckValid(state, action)):
        v = min(v, self.MaxValue(self.Result(state, action, self.myLetter)))
        # print("min: " + str(v))
        self.finalAction = action
    return v
    
  def MaxValue(self, state):
    if (self.TerminalTest(state)):
      return self.Utility(state)
    v = -99
    for action in self.actionSet:
      # Only make valid actions
      if (self.CheckValid(state, action)):
        v = max(v, self.MinValue(self.Result(state, action, self.urLetter)))
        # print("max: " + str(v))
        self.finalAction = action
    return v

  def TerminalTest(self, state):
    return self.GoalTest(state, 'O') or self.GoalTest(state, 'X')
    
  def GoalTest(self, state, v):
    win = False
    if (state.grid [0] == v and state.grid [1] == v and state.grid [2] == v):
      win = True
    elif (state.grid [3] == v and state.grid [4] == v and state.grid [5] == v):
      win = True
    elif (state.grid [6] == v and state.grid [7] == v and state.grid [8] == v):
      win = True
    elif (state.grid [0] == v and state.grid [3] == v and state.grid [6] == v):
      win = True
    elif (state.grid [1] == v and state.grid [4] == v and state.grid [7] == v):
      win = True
    elif (state.grid [2] == v and state.grid [5] == v and state.grid [8] == v):
      win = True
    elif (state.grid [0] == v and state.grid [4] == v and state.grid [8] == v):
      win = True
    elif (state.grid [2] == v and state.grid [4] == v and state.grid [6] == v):
      win = True
    #print(win)
    return win
    
  def CheckValid(self, state, action):
    return state.grid[int(action)-1] != 'O' and state.grid[int(action)-1] != 'X'
    
  def Result(self, state, action, letter):
    newState = State(state.grid)
    newState.grid[int(action)-1] = letter
    # print("new result")
    # print(newState)
    return newState
    
  def Utility(self, state):
    u = 0
    if (self.GoalTest(state, 'O')):
      if (self.myLetter == 'O'):
        u = 1
      else:
        u = -1
    elif (self.GoalTest(state, 'X')):
      if (self.myLetter == 'X'):
        u = 1
      else:
        u = -1
    else:
      u = 0
    #print(state)
    #print("U: " + str(u))
    #print("---")
    return u
  