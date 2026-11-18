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
        self.player=Player()
        self.tails=[]
        self.drag=False

class Player:
    def __init__(self):
        self.pos=pygame.Vector2(500,500)
        self.m=1
        self.direction=pygame.Vector2(0,0)
        self.speed=0.3
        self.going=False
        self.radius=10
    def draw(self):
        self.pos+=self.direction*self.speed
        if self.going: pygame.draw.circle(screen,(54,149,245),self.pos,self.radius)
        else: pygame.draw.circle(screen,(125,125,125),self.pos,self.radius)
class Tail:
    def __init__(self,pos,radius):
        self.pos=pygame.Vector2(pos)
        self.radius=radius
    def draw(self,dt):
        self.radius-=dt*50
        pygame.draw.circle(screen,(54,149,245),self.pos,max(0,int(self.radius)))

        