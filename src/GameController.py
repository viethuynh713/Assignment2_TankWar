import sys
import pygame
from pygame.locals import *
from pygame.math import *
from Bullet.BulletManager import BulletManager

from Constant import *
from EnumClass import *
from Player.PlayerManager import PlayerManager
from Wall.EdgeManager import EdgeManager


vector2 = pygame.math.Vector2
class GameController():
    def __init__(self):
        self.state = GameState.PLAYING
        self.mode = Mode.PVP
        self.mainPlayers = PlayerManager(PlayerType.MAIN)
        self.extraPlayers = PlayerManager(PlayerType.EXTRA)
        #self.bot
        self.maxPlayer = 2;
        self.InitGame()
        self.edgeManager = EdgeManager()
        self.bulletManager = BulletManager()
        self.Play()

    def InitGame(self):
        if self.mode == Mode.PVP:
            for i in range(self.maxPlayer):
                self.mainPlayers.InitOnePlayer(vector2(100,i*300 + 100))
                self.extraPlayers.InitOnePlayer(vector2(1000,i*300 + 100))
        if self.mode == Mode.PVE:
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

        self.bulletManager.createBullet(Vector2(500, 400), Vector2.rotate(UNIT_VECTOR, 30))

        # Set icon for the game
        while True:
            self.screen.fill((200,255,255))
            self.screen.blit(icon,(100,100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        icon = pygame.transform.rotate(icon,10)
                    elif event.key == K_2:
                        icon = pygame.transform.rotate(icon,-10)
                        
                        
                
            self.extraPlayers.Update(self.state,self.screen,self.bulletManager)
            self.mainPlayers.Update(self.state,self.screen,self.bulletManager)
            self.edgeManager.draw(self.screen)
            self.bulletManager.moveAllBullet(self.screen, self.edgeManager)
            
            pygame.display.update()
            self.clock.tick(FPS)

    def endGame(self):
        pass

    def resetGame(self):
        pass
    def HandleEventUI(self):
        pass
        