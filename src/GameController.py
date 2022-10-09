import sys
import pygame
from pygame.locals import *
from pygame.math import *
from Bullet.BulletManager import BulletManager

from Constant import *
from Wall.EdgeManager import EdgeManager

class GameController():
    def __init__(self):
        self.edgeManager = EdgeManager()
        self.bulletManager = BulletManager()
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

        self.edgeManager.createEdge(Vector2(100, 100), Vector2(1180, 100))
        self.edgeManager.createEdge(Vector2(1180, 100), Vector2(1180, 620))
        self.edgeManager.createEdge(Vector2(1180, 620), Vector2(100, 620))
        self.edgeManager.createEdge(Vector2(100, 620), Vector2(100, 100))

        self.edgeManager.createEdge(Vector2(700, 700), Vector2(400, 300))

        self.bulletManager.createBullet(Vector2(300, 400), Vector2.rotate(UNIT_VECTOR, 180))

        # Set icon for the game
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.edgeManager.draw(self.screen)
            self.bulletManager.moveAllBullet(self.screen, self.edgeManager)
            
            pygame.display.update()
            self.clock.tick(FPS)

    def endGame(self):
        pass

    def resetGame(self):
        pass