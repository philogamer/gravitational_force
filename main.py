import pygame
import random
import math
import function as fun
import sys

pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1400,700))
transparentscreen=pygame.Surface((1400,700), pygame.SRCALPHA)
pygame.display.set_caption('flyingstar')
clock=pygame.time.Clock()

msto=fun.Mapstore()
csto=fun.Constore()

#game loop
while True:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        fun.drag(msto,csto,event)
        if event.type==pygame.MOUSEWHEEL and not msto.player.going:
            if event.y>0: csto.zoom+=1*dt
            elif event.y<0: csto.zoom-=1*dt
            if csto.zoom>1:csto.zoom=1
            if csto.zoom<0.15:csto.zoom=0.15
        keys=pygame.key.get_pressed()
        if keys[pygame.K_n] and not csto.rendermap:
            csto.rendermap=True
        if keys[pygame.K_p] and not csto.rendermap:
            msto.player.going=False
            msto.player.speedvector=pygame.Vector2(0,0)
    if csto.rendermap:
        msto=fun.Mapstore()
    fun.makeuniverse(msto,csto)
    fun.zoom(msto,csto)
    fun.stay(msto)
    fun.gravitationalforce(msto,dt)
    fun.drawtail(msto)
    pygame.draw.circle(screen,(225,0,0),(70,70),50)
    fun.drawgame(msto,csto,dt)
    
    
    
    pygame.display.update()