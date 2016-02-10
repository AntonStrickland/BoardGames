import pygame
import sys 

screen = pygame.display.set_mode((640,480))
pygame.init()
normalFont = pygame.font.SysFont("monospace", 15)
gameFont = pygame.font.SysFont("monospace", 40)
delayTime = 10

colorOrange = (255,165,0)
colorBlack = (0,0,0)

def visualize():
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
  
  # update the screen
  pygame.display.update()
  pygame.time.delay(delayTime)