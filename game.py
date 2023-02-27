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

    def process_events(self):
        for event in pygame.event.get(): # User action
            if event.type == pygame.QUIT: # If user clicks exit
                return True
            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about:
                        if self.menu.state == 0:
                            # Start section of main menu
                            self.__init__()
                            self.game_over = False
                        elif self.menu.stae == 1:
                            # About section of main menu
                            self.about = True
                        elif self.menu.state == 2:
                            # Exit
                            return True


                # event keys for player movement and exit
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()

                elif event.key == pygame.K_LEFT:
                    self.player.move_left()

                elif event.key == pygame.K_UP:
                    self.player.move.up()

                elif event.key == pygame.K_DOWN:
                    self.player.move_down()

            # stopping player movement in game
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.stop_move_left()
                elif event.key == pygame.K_UP:
                    self.player.stop_move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.stop_move_down()

        return False

# write run_logic() here...
def run_logic(self):
    if not self.game_over:
        self.player.update(self.horizontal_blocks,self.vertical_blocks)
        block_hit_list = pygame.sprite.spritecollide(self.player,self.dots_group,True)
        
        if len(block_hit_list) > 0: # if pacman collects a dot... 
            # triggers the sound effect
            self.pacman_sound.play()
            self.score += 1
        
        block_hit_list = pygame.sprite.spritecollide(self.player,self.enemies,True)
        if len(block_hit_list) > 0:
            # if pacman collides with a ghost, it will trigger the explosion sound
            # and play the game over sound
            self.player.explosion = True
            self.game_over_sound.play()
        self.game_over = self.player.game_over
        self.enemies.update(self.horizontal_blocks,self.vertical_blocks)
        # here is the code to add a final score screen
        # tkMessageBox.showinfo("GAME OVER!", "Final Score = "+(str)(GAME.score))








