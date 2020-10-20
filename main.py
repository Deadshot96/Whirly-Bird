import os
import math
import time
import random
import pygame
from settings import *
from player import Player
import colors

class Game:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = FPS
        self.win = None
        self.gameWin = None
        self.clock = None
        self.titleFont = None
        self.textFont = None
        self.gameWidth = GW_WIDTH
        self.gameHeight = GW_HEIGHT
        self.xoff = XOFF
        self.yoff = YOFF
        self.gameStart = False
        self.player = None

    
    def game_init(self):
        # init
        pygame.init()
        pygame.font.init()

        # windows init
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Whirly Bird")
        self.win.fill(colors.MID_BLACK)
        
        self.gameWin = self.win.subsurface((self.xoff,\
            self.yoff, self.gameWidth, self.gameHeight))

        # fonts init
        self.titleFont = pygame.font.SysFont('comicsansms', FONT_SIZE)
        self.textFont = pygame.font.SysFont('impact', int(FONT_SIZE // 1.5))
        
        # Block for Title 
        title = self.titleFont.render('Whirly Bird Developer', 1, colors.GOLD)
        fontX = (self.win.get_width() - title.get_width()) // 2
        fontY = (YOFF - title.get_height()) // 2

        # Background
        self.win.blit(title, (fontX, fontY))

        # Clock init
        self.clock = pygame.time.Clock()

    def draw(self):
        self.gameWin.fill(colors.MINT_CREAM)

        if not self.gameStart:
            text = self.textFont.render('Press Enter to start the game', 1, colors.SADDLE_BROWN)
            textX = (self.gameWin.get_width() - text.get_width()) // 2
            textY = self.yoff + (self.gameWin.get_width() - text.get_height()) // 2
        
            self.gameWin.blit(text, (textX, textY))

        if self.gameStart:
            self.player.move()
            self.player.draw(self.gameWin)

        pygame.display.update()

    def new_game(self):
        x = self.gameWidth // 2
        y = self.gameHeight // 2
        self.player = Player(x, y)


    def run(self):
        self.game_init()
        self.draw()

        run = True
        while run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()

                    if pressed[pygame.K_RETURN]:
                        self.gameStart = True
                        self.new_game()

                    if pressed[pygame.K_UP]:
                        self.player.jump()

                    if pressed[pygame.K_DOWN]:
                        pass

                    if pressed[pygame.K_RIGHT]:
                        self.player.push_right()

                    if pressed[pygame.K_LEFT]:
                        self.player.push_left()
                
                # if event.type == pygame.KEYUP:
                #     self.player.stop_push()

            self.draw()

        pygame.font.quit()
        pygame.quit()

if __name__ == "__main__":
    X = Game()
    X.run()
