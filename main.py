import pygame
import random
import math
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1500,800))
transparentscreen=pygame.Surface((1500,800), pygame.SRCALPHA)
pygame.display.set_caption('Lost Soul')
clock=pygame.time.Clock()



#game loop
while True:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    
    
    
    
    pygame.display.update()