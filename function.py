import pygame
import random
import math
from information import *
pygame.init()
pygame.mixer.init()
pygame.font.init()


def drawgame(msto,dt):
    screen.fill((0,0,0))
    transparentscreen.fill((0,0,0,210))
    for i in msto.stars:
        i.draw()
    drawdrag(msto)
    for i in msto.planets:
        i.draw()
    screen.blit(transparentscreen)
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
        if pygame.math.Vector2.magnitude(msto.player.pos-take)>200:
            take=msto.player.pos-pygame.math.Vector2.normalize(msto.player.pos-take)*200
        msto.player.speedvector=pygame.math.Vector2(msto.player.pos-take)*0.3
def drawtail(msto):
    msto.tails.append(Tail(msto.player.pos,msto.player.radius))
    for i in msto.tails:
        if i.radius<=0:
            msto.tails.remove(i)
def drawdrag(msto):
    if msto.drag and not msto.player.going:
        pos1=pygame.Vector2(pygame.mouse.get_pos())
        if pygame.math.Vector2.magnitude(msto.player.pos-pos1)>200:
            pos1=msto.player.pos-pygame.math.Vector2.normalize(msto.player.pos-pos1)*200
        sidescale=pygame.math.Vector2.normalize(msto.player.pos-pos1)*(msto.player.radius-1)
        side=pygame.math.Vector2.rotate(sidescale,90)
        pos2=msto.player.pos+side
        pos3=msto.player.pos-side
        pygame.draw.polygon(screen,(225,225,225),(pos1,pos2,pos3))
def makeplanet(msto,csto):
    if csto.rendermap:
        locatex=list(range(80,1321))
        locatey=list(range(80,621))
        radiusgacha=list(range(30,71))
        while len(msto.planets)<=9:
            testx=[]
            testy=[]
            radius=random.choice(radiusgacha)
            GM=random.randint(3000,12000)
            for i in locatex:
                testx.append(i)
            for i in locatey:
                testy.append(i)
            x=random.choice(testx)
            y=random.choice(testy)
            while x-radius not in locatex or x+radius not in locatex or y-radius not in locatey or y+radius not in locatey:
                x=random.choice(testx)
                if x-radius not in locatex or x+radius not in locatex: testx.remove(x)
                y=random.choice(testy)
                if y-radius not in locatey or y+radius not in locatey: testy.remove(y)
                if len(testx)==0 or len(testy)==0:
                    radiusgacha.remove(radius)
                    break
            if  len(testx)!=0 and len(testy)!=0: 
                msto.planets.append(Planet(radius,x,y,GM))
                for i in range(x-radius-10,x+radius+10):
                    if i in locatex: locatex.remove(i)
                for i in range(y-radius-10,y+radius+10):
                    if i in locatey: locatey.remove(i)
            if len(locatex)==0 or len(locatey)==0 or len(radiusgacha)==0: break
        star(msto)
        csto.rendermap=False
def gravitationalforce(msto,dt):
    if msto.player.going:
        for i in msto.planets:
            msto.player.speedvector+=i.GM/pygame.math.Vector2.magnitude_squared(i.pos-msto.player.pos)*dt*(i.pos-msto.player.pos)
def star(msto):
    num=random.randint(20,40)
    testx=list(range(80,1321))
    testy=list(range(80,621))
    for i in range(0,num+1):
        x=random.choice(testx)
        testx.remove(x)
        y=random.choice(testy)
        testy.remove(y)
        msto.stars.append(Planet(2,x,y,0))
def stay(msto):
    for i in msto.planets:
        if pygame.math.Vector2.magnitude(i.pos-msto.player.pos)<=i.radius:
            msto.player.speedvector=pygame.Vector2(0,0)
            r=pygame.math.Vector2.normalize(i.pos-msto.player.pos)*(msto.player.radius+i.radius)
            msto.player.pos=i.pos-r
            msto.player.going=False