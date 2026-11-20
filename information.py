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
        if self.going: pygame.draw.circle(screen,(54,149,245),self.showpos,self.radius)
        else: pygame.draw.circle(screen,(125,125,125),self.showpos,self.radius)
class Tail:
    def __init__(self,pos,radius):
        self.pos=pygame.Vector2(pos)
        self.speedratio=0.03
        self.radius=radius
    def draw(self,dt,speedvector):
        self.pos-=speedvector*self.speedratio
        self.radius-=dt*20
        pygame.draw.circle(screen,(54,149,245),self.pos,max(0,int(self.radius)))
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
    def draw(self,pos):
        for i in range(self.radius,0,-1):
            pygame.draw.circle(transparentscreen,(self.a,self.b,self.c,3*i),self.pos+pos,i)
        if self.radius==2:
            pygame.draw.circle(transparentscreen,(self.a,self.b,self.c,255),self.pos+pos,self.radius)
        pygame.draw.circle(transparentscreen,(self.c,self.a,self.b,255),self.pos+pos,self.mradius,1)
        

        