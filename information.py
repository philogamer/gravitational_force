import pygame
import random
import math
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1500,800))
transparentscreen=pygame.Surface((1500,800), pygame.SRCALPHA)
pygame.display.set_caption('Lost Soul')