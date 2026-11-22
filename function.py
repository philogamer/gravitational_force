import pygame
import random
import math
from information import *
pygame.init()
pygame.mixer.init()
pygame.font.init()


def drawgame(msto,csto,dt):
    screen.fill((0,0,0))
    transparentscreen.fill((0,0,0,210))
    for i in msto.stars:
        i.draw(msto.player.showpos-msto.player.pos)
    drawdrag(msto,csto)
    for i in msto.planets:
        i.draw(msto.player.showpos-msto.player.pos)
    for i in msto.tails:
        i.draw(dt,msto.player.speedvector)
    screen.blit(transparentscreen)
    msto.player.draw()
def drag(msto,csto,event):
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and not msto.player.going and csto.zoom==1:
        msto.drag=True
    if event.type==pygame.MOUSEBUTTONUP and event.button==1 and not msto.player.going and csto.zoom==1:
        msto.player.going=True
        msto.drag=False
        take=pygame.Vector2(pygame.mouse.get_pos())
        if pygame.math.Vector2.magnitude(msto.player.showpos-take)>200:
            take=msto.player.showpos-pygame.math.Vector2.normalize(msto.player.showpos-take)*200
        msto.player.speedvector=pygame.math.Vector2(msto.player.showpos-take)*0.7
def drawtail(msto):
    msto.tails.append(Tail(msto.player.showpos,msto.player.radius))
    for i in msto.tails:
        if i.radius<=0:
            msto.tails.remove(i)
def drawdrag(msto,csto):
    if msto.drag and not msto.player.going and csto.zoom==1:
        pos1=pygame.Vector2(pygame.mouse.get_pos())
        if pygame.math.Vector2.magnitude(msto.player.showpos-pos1)>200:
            pos1=msto.player.showpos-pygame.math.Vector2.normalize(msto.player.showpos-pos1)*200
        sidescale=pygame.math.Vector2.normalize(msto.player.showpos-pos1)*(msto.player.radius-1)
        side=pygame.math.Vector2.rotate(sidescale,90)
        pos2=msto.player.showpos+side
        pos3=msto.player.showpos-side
        pygame.draw.polygon(screen,(225,225,225),(pos1,pos2,pos3))
def makeplanet(msto,csto,locatex,locatey):
    count=0
    radiusgacha=list(range(50,101))
    star(msto,locatex,locatey)
    while count<=random.randint(2,4):
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
                            if radius<40: skip=True
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
        if not skip: 
            msto.planets.append(Planet(radius,x,y,GM))
            count+=1
        if x in locatex: locatex.remove(x)
        if y in locatey: locatey.remove(y)
        if len(locatex)==0 or len(locatey)==0: break
        
def makeuniverse(msto,csto):
    if csto.rendermap:    
        for i in range(-4,4):
            for j in range(-4,4):
                a=-1400+i*1400
                b=-700+j*700
                locatex=list(range(a,a+1400))
                locatey=list(range(b,b+700))
                makeplanet(msto,csto,locatex,locatey)
        csto.rendermap=False
def gravitationalforce(msto,dt):
    if msto.player.going:
        for i in msto.planets:
            msto.player.speedvector+=i.GM/pygame.math.Vector2.magnitude_squared(i.pos-msto.player.pos)*dt*(i.pos-msto.player.pos)
def star(msto,testx,testy):
    num=random.randint(20,40)
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
def zoom(msto,csto):
    take=pygame.Vector2(msto.player.pos)
    for i in msto.planets:
        i.radius=i.radius/csto.previouszoom*csto.zoom
        i.mradius=i.mradius/csto.previouszoom*csto.zoom
        r=(i.pos-take)/csto.previouszoom*csto.zoom
        i.pos=take+r
    for i in msto.stars:
        r=(i.pos-take)/csto.previouszoom*csto.zoom
        i.lightforstar=i.lightforstar/csto.previouszoom*csto.zoom
        i.pos=take+r
    msto.player.radius=msto.player.radius/csto.previouszoom*csto.zoom
    csto.previouszoom=csto.zoom

#def replay