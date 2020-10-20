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
        self.gameWidth = GW_WIDTH
        self.gameHeight = GW_HEIGHT
        self.xoff = XOFF
        self.yoff = YOFF

    
    def game_init(self):

        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Whirly Bird")
        self.win.fill(colors.MID_BLACK)
        
        self.gameWidth = self.win.subsurface((self.xoff,\
            self.yoff, self.gameWidth, self.gameHeight))

        self.font = pygame.font.SysFont('comicsansms', FONT_SIZE)
        
        title = self.font.render('Whirly Bird Developer', 1, colors.GOLD)
        fontX = (self.win.get_width() - title.get_width()) // 2
        fontY = (YOFF - title.get_height()) // 2

        self.win.blit(title, (fontX, fontY))
        
        self.clock = pygame.time.Clock()

    def draw(self):
        self.gameWidth.fill(colors.MINT_CREAM)
        pygame.display.update()

    def run(self):
        self.game_init()
        self.draw()

        run = True
        while run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

            self.draw()

        pygame.font.quit()
        pygame.quit()

if __name__ == "__main__":
    X = Game()
    X.run()
