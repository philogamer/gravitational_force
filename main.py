import pygame
import random
import math
import function as fun

pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1400,700))
transparentscreen=pygame.Surface((1400,700), pygame.SRCALPHA)
pygame.display.set_caption('Lost Soul')
clock=pygame.time.Clock()

csto=fun.Constore()

#game loop
while True:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        fun.drag(csto,event)
    fun.drawtail(csto)
    pygame.draw.circle(screen,(225,0,0),(70,70),50)
    fun.drawgame(csto,dt)
    
    
    
    pygame.display.update()