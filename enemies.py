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


# Slime class creation
class Slime(pygame.sprite.Sprite):
    def __init__(self,x,y,change_x,change_y):

        # call parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # set the direction of the slime (ghosts)
        self.change_x = change_x
        self.change_y = change_y

        # load the imgage of the ghosts
        self.image = pygame.image.load("slime.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    # update function
    def update(self,horizontal_blocks,vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        # setting the movement for the ghosts
        # allowing them to pass through each other (intersect)
        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left","right","up","down"))

            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0

            if direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0

            if direction == "up" and self.change_x == 0:
                self.change_x = 0
                self.change_y = -2

            if direction == "down" and self.change_x == 0:
                self.change_x = 0
                self.change_y = 2


    # get_intersection_position function
    def get_intersection_position(self):
        items = []
        for i,row in enumerate(environment()):
            for j,item in enumerate(row):
                if item == 3:
                    items.append((j*32,i*32))

        return items

# making the environment (the maze that pacman and the ghosts move through)
def environment():

# this is the basic grid used from pygame maze examples and pacman game examples
    grid = ((0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0))

    return grid

# drawing the environment
# template code to draw the env == pygame.draw.line(surface, color, start_pos, end_pos)
def draw_environment():
    for i,row in enumerate(environment()):
        for j,item in enumerate(row):
            if item == 1:
                pygame.draw.line(screen, BLUE, [j*32, i*32], [j*32+32,i*32], 3)
                pygame.draw.line(screen, BLUE, [j*32, i*32+32], [j*32+32, i*32+32], 3)
            elif item == 2:
                pygame.draw.line(screen, BLUE, [j*32, i*32], [j*32,i*32+32], 3)
                pygame.draw.line(screen, BLUE, [j*32+32, i*32], [j*32+32,i*32+32], 3)
