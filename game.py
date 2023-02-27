import pygame
from player import Player
from enemies import *
import tkinter
from tkinter import messagebox
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Game(object):
    def __init__(self):
        self.font = pygame.font.Font(SysFont, 40)
        self.about = False
        self.game_over = True
        
        # create score variable
        self.score = 0
        # create font that displays user score
        self.font = pygame.font.Font(SysFont, 25)
        # create start meny
        self.menu = Menu(("Start","About","Exit"),font_color = WHITE,font_size=55)
        # create player, using pacman img
        self.player = Player(32,128,"player.png")
        
        # make blocks that set paths for player movement
        self.horizontal_blocks = pygame.sprite.Group()
        self.vertical_blocks = pygame.sprite.Group()

        # create a group for the dots pacman collects
        self.dots_group = pygame.sprite.Group()

        # set the environment
        for i, row in enumerate(environment()):
            if item == 1:
                self.horizontal_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
            elif item == 2:
                self.vertical_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))

        # make the ghosts (enemies)
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Slime(288,96,0,2))
        self.enemies.add(Slime(288,320,0,-2))
        self.enemies.add(Slime(544,128,0,2))
        self.enemies.add(Slime(32,224,0,2))
        self.enemies.add(Slime(160,64,2,0))
        self.enemies.add(Slime(448,64,-2,0))
        self.enemies.add(Slime(640,448,2,0))
        self.enemies.add(Slime(448,320,2,0))

        # add the dots that pacman collects
        for i, row in enumerate(()):
            for j, item in enumerate(row):
                if item != 0:
                    self.dots_group.add(Ellipse(j*32+12,i*32+12,WHITE,8,8))

        # add sound effects
        self.pacman_sound = pygame.mixer.Sound("pacman_sound.ogg")
        self.game_over_sound = pygame.mixer.Sound("game_over_sound.ogg")


        