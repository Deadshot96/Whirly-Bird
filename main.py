import os
import math
import time
import random
import pygame
from settings import *
import colors

class Game:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = FPS
        self.win = None
        self.clock = None
        self.font = None
    
    def game_init(self):

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Whirly Bird")

        self.win.fill(colors.MINT_CREAM)

        self.clock = pygame.time.Clock()

    def run(self):
        self.game_init()

        run = True
        while run:
            self.clock.tick(self.fps)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()

if __name__ == "__main__":
    X = Game()
    X.run()
