import sys
import pygame
from pygame.locals import *

from Constant import *

class GameController():
    def __init__(self):
        self.Play()
    def InitGame(self):
        pass
    def Play(self):
        # Initialize
        pygame.init()
        self.clock = pygame.time.Clock()
        # Set Resolution
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        # Set name of the game
        pygame.display.set_caption("Tank War")
        # Set icon for the game
        icon = pygame.image.load("../asset/icon/war.png")
        pygame.display.set_icon(icon)
        # Set icon for the game
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    def endGame(self):
        pass
    def resetGame(self):
        pass