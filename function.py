import pygame
import random
import math
from information import *
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1400,700))
transparentscreen=pygame.Surface((1400,700), pygame.SRCALPHA)


def drawgame(csto,dt):
    screen.fill((0,0,0))
    drawdrag(csto)
    for i in csto.tails:
        i.draw(dt)
    csto.player.draw()
    
def drag(csto,event):
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        csto.drag=True
    if event.type==pygame.MOUSEBUTTONUP and event.button==1 and csto.drag:
        csto.player.going=True
        csto.drag=False
        take=pygame.Vector2(pygame.mouse.get_pos())
        csto.player.speed=pygame.math.Vector2.magnitude(take)*0.01
        csto.player.direction=pygame.math.Vector2.normalize(csto.player.pos-take)
def drawtail(csto):
    csto.tails.append(Tail(csto.player.pos,csto.player.radius))
    for i in csto.tails:
        if i.radius<=0:
            csto.tails.remove(i)
def drawdrag(csto):
    if csto.drag:
        pos1=pygame.Vector2(pygame.mouse.get_pos())
        sidescale=pygame.math.Vector2.normalize(csto.player.pos-pos1)*csto.player.radius
        side=pygame.math.Vector2.rotate(sidescale,90)
        pos2=csto.player.pos+side
        pos3=csto.player.pos-side
        pygame.draw.polygon(screen,(225,225,225),(pos1,pos2,pos3))