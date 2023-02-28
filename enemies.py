# import necessary modules
import pygame
import random

# set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# define colors
BLACK = (0,0,0)
WHTIE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

# Block class creation
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,color,width,height):

        # call parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # set background color (and make it transparent)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)


# Ellipse class creation
class Ellipse(pygame.sprite.Sprite):
    def __init__(self,x,y,color,width,height):

        # call parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # set background color (and make it black)
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # drawing the ellipse
        pygame.draw.ellipse(self.image,color,[0,0,width,height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

