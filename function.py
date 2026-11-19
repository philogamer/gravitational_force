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
        move=False
        locatex=list(range(80,1321))
        locatey=list(range(80,621))
        radiusgacha=list(range(30,71))
        while len(msto.planets)<=random.randint(7,11):
            move=False
            skip=False
            x=random.choice(locatex)
            y=random.choice(locatey)
            radius=random.choice(radiusgacha)
            pos=pygame.Vector2(x,y)
            GM=random.randint(3000,12000)
            if msto.planets:
                for i in msto.planets:
                    dis=i.pos-pos
                    if pygame.math.Vector2.magnitude(dis)<(radius+i.radius+20):
                        dis=pygame.math.Vector2.normalize(dis)*(radius+i.radius+21)
                        pos=i.pos-dis
                        move=True
                        endx=i.x
                        endy=i.y
                        for j in msto.planets:
                            if i.pos==j.pos: break
                            dis=j.pos-pos
                            if pygame.math.Vector2.magnitude(dis)<(radius+j.radius+20):
                                radius=int(abs(pygame.math.Vector2.magnitude(dis)-j.radius-20))
                                if radius<30: skip=True
            if move:
                x=int(pos.x)
                y=int(pos.y)
                if endx>x: 
                    for i in range(x+1,endx):
                        if i in locatex:
                            locatex.remove(i)
                elif endx<x: 
                    for i in range(endx,x):
                        if i in locatex:
                            locatex.remove(i)
                if endy>y: 
                    for i in range(y+1,endy):
                        if i in locatey:
                            locatey.remove(i)
                elif endy<y: 
                    for i in range(endy,y):
                        if i in locatey:
                            locatey.remove(i)
            if not skip: msto.planets.append(Planet(radius,x,y,GM))
            if x in locatex: locatex.remove(x)
            if y in locatey: locatey.remove(y)
            if len(locatex)==0 or len(locatey)==0: break
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
def removeoutside(msto):
    for i in msto.planets:
        if i.x<0 or i.y<0 or i.x>1400 or i.y>700:
            msto.planets.remove(i)