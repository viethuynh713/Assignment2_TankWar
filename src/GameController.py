import sys
import pygame
from pygame.locals import *

from Constant import *
from EnumClass import *
from Player.PlayerManager import PlayerManager


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
                        
                        
                
            self.extraPlayers.Update(self.state,self.screen)
            self.mainPlayers.Update(self.state,self.screen)
            pygame.display.update()
            
                            
                            
                    
    def endGame(self):
        pass
    def resetGame(self):
        pass
    def HandleEventUI(self):
        pass
        