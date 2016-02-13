import pygame
import sys 

screen = pygame.display.set_mode((640,480))
pygame.init()
normalFont = pygame.font.SysFont("monospace", 15)
gameFont = pygame.font.SysFont("monospace", 100)
delayTime = 10

colorOrange = (255,165,0)
colorBlack = (0,0,0)

def visualize(grid):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # if event.type == pygame.KEYDOWN:
    #   if event.key == pygame.K_1:
    #     location -= 1
    #   if event.key == pygame.K_RIGHT:
    #     location += 1
      
  screen.fill(colorBlack)
  
  pygame.draw.lines(screen, colorOrange, False, [(250, 100), (250, 400)], 5)
  pygame.draw.lines(screen, colorOrange, False, [(150, 200), (450, 200)], 5)
  pygame.draw.lines(screen, colorOrange, False, [(350, 100), (350, 400)], 5)
  pygame.draw.lines(screen, colorOrange, False, [(150, 300), (450, 300)], 5)
  
  l1 = gameFont.render(str(grid[0]), 1, (255,255,0))
  l2 = gameFont.render(str(grid[1]), 1, (255,255,0))
  l3 = gameFont.render(str(grid[2]), 1, (255,255,0))
  l4 = gameFont.render(str(grid[3]), 1, (255,255,0))
  l5 = gameFont.render(str(grid[4]), 1, (255,255,0))
  l6 = gameFont.render(str(grid[5]), 1, (255,255,0))
  l7 = gameFont.render(str(grid[6]), 1, (255,255,0))
  l8 = gameFont.render(str(grid[7]), 1, (255,255,0))
  l9 = gameFont.render(str(grid[8]), 1, (255,255,0))
  
  # draw the X's and O's
  screen.blit(l2, (270,100))
  screen.blit(l5, (270,200))
  screen.blit(l8, (270,300))
  
  screen.blit(l1, (170,100))
  screen.blit(l4, (170,200))
  screen.blit(l7, (170,300))
  
  screen.blit(l3, (370,100))
  screen.blit(l6, (370,200))
  screen.blit(l9, (370,300))
  
  # update the screen
  pygame.display.update()
  pygame.time.delay(delayTime)