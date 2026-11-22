import pygame
import random
import math
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1400,700))
transparentscreen=pygame.Surface((1400,700), pygame.SRCALPHA)

class Constore:
    def __init__(self):
        self.rendermap=True
        self.previouszoom=1
        self.zoom=1
class Mapstore:
    def __init__(self):
        self.player=Player()
        self.tails=[]
        self.drag=False
        self.planets=[]
        self.stars=[]

class Player:
    def __init__(self):
        self.pos=pygame.Vector2(700,350)
        self.showpos=pygame.Vector2(700,350)
        self.m=1
        self.speedvector=pygame.Vector2(0,0)
        self.speedratio=0.3
        self.going=False
        self.radius=10
    def draw(self):
        self.pos+=self.speedvector*self.speedratio
        if self.going: pygame.draw.circle(screen,(250,250,250),self.showpos,self.radius)
        else: pygame.draw.circle(screen,(125,125,125),self.showpos,self.radius)
class Tail:
    def __init__(self,pos,radius):
        self.pos=pygame.Vector2(pos)
        self.speedratio=0.03
        self.radius=radius
    def draw(self,dt,speedvector):
        self.pos-=speedvector*self.speedratio
        a=min(speedvector.length()/150,1)
        r = 255 if a < 0.6 else int(255 - (a - 0.6) / 0.4 * 155)
        g = int(50 + a / 0.5 * 205) if a < 0.5 else int(255 - (a - 0.5) / 0.5 * 205)
        b = 0 if a < 0.4 else int((a - 0.4) / 0.6 * 255)
        self.radius-=dt*15
        pygame.draw.circle(transparentscreen,(r,g,b,max(0,int(self.radius*25))),self.pos,max(0,int(self.radius)))
class Planet:
    def __init__(self,radius,x,y,GM):
        self.x=x
        self.y=y
        self.radius=radius
        self.pos=pygame.Vector2(x,y)
        self.GM=GM
        self.mradius=self.GM/50
        self.a=random.randint(100,255)
        self.b=random.randint(100,255)
        self.c=random.randint(100,255)
        self.lightforstar=255
    def draw(self,pos):
        a=self.radius/255
        for i in range(round(self.radius),0,-1):
            pygame.draw.circle(transparentscreen,(self.a,self.b,self.c,a*i),self.pos+pos,i)
        if self.radius==2:
            pygame.draw.circle(transparentscreen,(self.a,self.b,self.c,self.lightforstar),self.pos+pos,self.radius)
        pygame.draw.circle(transparentscreen,(self.c,self.a,self.b,255),self.pos+pos,self.mradius,1)
        

        