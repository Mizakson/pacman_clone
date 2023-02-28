# import neccessary modules and constants

import pygame
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# main function
def main():

    # initialize all imported pygame modules
    pygame.init()

    # set the width and height of the screen display [width (800), height(576)]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # set window caption
    pygame.display.set_caption("PACMAN CLONE -- Mizakson")

    # loop until user hits the close button or exits
    done = False

    # manage how fast the screen updates
    clock = pygame.time.Clock()

    # create a game object
    game = Game()


    # Main program loop
    while not done:
        # process keystrokes, clicks, etc...
        done = game.process_events()

        # game logic
        game.run_logic()

        # display the current frame
        game.display_frame(screen)

        # limit game to 30 fps
        clock.tick(30)

        # final score message 
        tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(Game.score))


    # exit the game
    pygame.quit()


# run the main file
if __name__ == '__main__':
    main()

