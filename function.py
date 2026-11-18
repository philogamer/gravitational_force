import pygame
import random
import math
from information import *
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1400,700))
transparentscreen=pygame.Surface((1400,700), pygame.SRCALPHA)


def drawgame(msto,dt):
    screen.fill((0,0,0))
    for i in msto.planets:
        i.draw()
    drawdrag(msto)
    for i in msto.tails:
        i.draw(dt)
    msto.player.draw()    
def drag(msto,event):
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        msto.drag=True
    if event.type==pygame.MOUSEBUTTONUP and event.button==1 and not msto.player.going:
        msto.player.going=True
        msto.drag=False
        take=pygame.Vector2(pygame.mouse.get_pos())
        msto.player.speedvector=pygame.math.Vector2(msto.player.pos-take)*0.1
def drawtail(msto):
    msto.tails.append(Tail(msto.player.pos,msto.player.radius))
    for i in msto.tails:
        if i.radius<=0:
            msto.tails.remove(i)
def drawdrag(msto):
    if msto.drag and not msto.player.going:
        pos1=pygame.Vector2(pygame.mouse.get_pos())
        sidescale=pygame.math.Vector2.normalize(msto.player.pos-pos1)*msto.player.radius
        side=pygame.math.Vector2.rotate(sidescale,90)
        pos2=msto.player.pos+side
        pos3=msto.player.pos-side
        pygame.draw.polygon(screen,(225,225,225),(pos1,pos2,pos3))
def makeplanet(msto,csto):
    if csto.rendermap:
        locatex=list(range(80,1320))
        locatey=list(range(80,620))
        for i in range (0,random.randint(9,15)):
            radius=random.randint(30,70)
            x=random.choice(locatex)
            y=random.choice(locatey)
            GM=random.randint(3000,12000)
            msto.GMpos.append(pygame.Vector2(x,y))
            msto.GMs.append(GM)
            msto.planets.append(Planet(radius,x,y,GM))
            for i in range(x-radius-110,x+radius+111):
                if i in locatex: locatex.remove(i)
            for i in range(y-radius-110,y+radius+111):
                if i in locatey: locatey.remove(i)
            if len(locatex)==0 or len(locatey)==0: break
        csto.rendermap=False
def gravitationalforce(msto,dt):
    if msto.player.going:
        for i in msto.planets:
            msto.player.speedvector+=i.GM/pygame.math.Vector2.magnitude_squared(i.pos-msto.player.pos)*dt*(i.pos-msto.player.pos)
                