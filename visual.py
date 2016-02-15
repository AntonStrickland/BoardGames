import pygame
import sys 

screen = pygame.display.set_mode((640,480))
pygame.init()
normalFont = pygame.font.SysFont("monospace", 15)
gameFont = pygame.font.SysFont("monospace", 100)
headerFont = pygame.font.SysFont("monospace", 30)
delayTime = 100

colorOrange = (255,165,0)
colorGray = (92, 92, 92)
colorBlack = (0,0,0)
colorWhite = (255, 255, 255)

treeList = []

class Visualizer():
  def __init__(self):
    self.x = 0
    self.y = 100
    
  def getInput(self):
    move = '.'
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          self.x -= 100
        if event.key == pygame.K_RIGHT:
          self.x += 100
        if event.key == pygame.K_1:
          move = '1'
        if event.key == pygame.K_2:
          move = '2'
        if event.key == pygame.K_3:
          move = '3'
        if event.key == pygame.K_4:
          move = '4'
        if event.key == pygame.K_5:
          move = '5'
        if event.key == pygame.K_6:
          move = '6'
        if event.key == pygame.K_7:
          move = '7'
        if event.key == pygame.K_8:
          move = '8'
        if event.key == pygame.K_9:
          move = '9'
          
    return move
    
  def visualizeTree(self):
    for node in treeList:
      visualize(node, x, y)
      pygame.display.update()
      pygame.time.delay(delayTime)
      
  def checkNextGame(self):
    move = '-'
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_y:
          move = 'Y'
        if event.key == pygame.K_n:
          move = 'N'
    return move
  
  def visualize(self, state, x, y):

    grid = state.grid
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
    screen.fill(colorBlack)
    
    pygame.draw.lines(screen, colorOrange, False, [(x+250, 100), (x+250, 400)], 5)
    pygame.draw.lines(screen, colorOrange, False, [(x+150, 200), (x+450, 200)], 5)
    pygame.draw.lines(screen, colorOrange, False, [(x+350, 100), (x+350, 400)], 5)
    pygame.draw.lines(screen, colorOrange, False, [(x+150, 300), (x+450, 300)], 5)
    
    header = None
    if (state.aiTurn is True):
      header = headerFont.render("AI's Turn", 1, colorWhite)
    else:
      header = headerFont.render("Player's Turn", 1, colorWhite)
    
    l1 = []
    for i in grid:
      if i == 'O' or i == 'X':
        l1.append(gameFont.render(str(i), 1, colorOrange))
      else:
        l1.append(gameFont.render(str(i), 1, colorGray))
       
    # draw the X's and O's
    
    screen.blit(header, (x+170,60))

    screen.blit(l1[0], (x+170,100))
    screen.blit(l1[3], (x+170,200))
    screen.blit(l1[6], (x+170,300))
    
    screen.blit(l1[1], (x+270,100))
    screen.blit(l1[4], (x+270,200))
    screen.blit(l1[7], (x+270,300))
    
    screen.blit(l1[2], (x+370,100))
    screen.blit(l1[5], (x+370,200))
    screen.blit(l1[8], (x+370,300))
    
    # update the screen
    pygame.display.update()
    pygame.time.delay(delayTime)