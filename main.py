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

msto=fun.Mapstore()
csto=fun.Constore()

#game loop
while True:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        fun.drag(msto,event)
    fun.makeplanet(msto,csto)
    fun.drawtail(msto)
    pygame.draw.circle(screen,(225,0,0),(70,70),50)
    fun.drawgame(msto,dt)
    
    
    
    pygame.display.update()