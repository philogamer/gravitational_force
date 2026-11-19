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
        self.pos=pygame.Vector2(500,500)
        self.m=1
        self.speedvector=pygame.Vector2(0,0)
        self.speedratio=0.3
        self.going=False
        self.radius=10
    def draw(self):
        self.pos+=self.speedvector*self.speedratio
        if self.going: pygame.draw.circle(screen,(54,149,245),self.pos,self.radius)
        else: pygame.draw.circle(screen,(125,125,125),self.pos,self.radius)
class Tail:
    def __init__(self,pos,radius):
        self.pos=pygame.Vector2(pos)
        self.radius=radius
    def draw(self,dt):
        self.radius-=dt*50
        pygame.draw.circle(screen,(54,149,245),self.pos,max(0,int(self.radius)))
class Planet:
    def __init__(self,radius,x,y,GM):
        self.radius=radius
        self.pos=pygame.Vector2(x,y)
        self.GM=GM
        a=random.randint(100,255)
        b=random.randint(100,255)
        c=random.randint(100,255)
        self.color=(a,b,c)
        self.gravitycolor=(c,a,b)
    def draw(self):
        pygame.draw.circle(screen,self.color,self.pos,self.radius)
        pygame.draw.circle(screen,self.gravitycolor,self.pos,self.GM/50,1)
        

        