import sys
import pygame
from pygame.locals import *
from pygame.math import *
from Bullet.BulletManager import BulletManager
from Button import *
import webbrowser
from enum import Enum
import random
import math

from Constant import *
from EnumClass import *
from Player.PlayerManager import PlayerManager
from Wall.EdgeManager import EdgeManager


vector2 = pygame.math.Vector2


class Result(Enum):
    LOSE = 0,
    WIN = 1;


class GameController():
    def __init__(self):
        self.isOpenSetting = False
        self.isMusicDisable = False
        self.isVolumeDisable = False
        self.resultPlayer1 = Result.LOSE
        self.resultPlayer2 = Result.WIN
        self.state = GameState.INIT
        self.mode = Mode.PVP
        #self.bot
        self.maxPlayer = 2;
        self.edgeManager = EdgeManager()
        self.bulletManager = BulletManager()
        self.mainPlayers = PlayerManager(PlayerType.MAIN, self.edgeManager)
        self.extraPlayers = PlayerManager(PlayerType.EXTRA, self.edgeManager)
        self.Play()

    def InitGame(self):
        if self.mode == Mode.PVP:
            for i in range(self.maxPlayer):
                self.mainPlayers.InitOnePlayer(vector2(101,i*301 + 101))
                self.extraPlayers.InitOnePlayer(vector2(1080,i*301 + 101))
        if self.mode == Mode.PVE:
            pass
        self.edgeManager.createEdge(Vector2(100, 100), Vector2(1180, 100))
        self.edgeManager.createEdge(Vector2(1180, 100), Vector2(1180, 620))
        self.edgeManager.createEdge(Vector2(1180, 620), Vector2(100, 620))
        self.edgeManager.createEdge(Vector2(100, 620), Vector2(100, 100))
        self.edgeManager.createEdge(Vector2(300, 200), Vector2(200, 300))
        self.edgeManager.createEdge(Vector2(980, 200), Vector2(1080, 300))
        self.edgeManager.createEdge(Vector2(200, 420), Vector2(300, 520))
        self.edgeManager.createEdge(Vector2(980, 520), Vector2(1080, 420))
        self.edgeManager.createEdge(Vector2(400, 320), Vector2(880, 320))
        self.edgeManager.createEdge(Vector2(400, 400), Vector2(880, 400))
            
    def HandleEventUI(self):
        
        self.screen.blit(self.backgroundInGame, (0,0))
        if self.state == GameState.INIT:
            # TODO: Draw panel game
            self.screen.blit(self.logo, (363, 40))

            if Button(530, 355, self.playButton, 1).draw(self.screen):
                self.isOpenSetting = False
                self.state = GameState.PLAYING
                self.InitGame()
                #playMusic(self.isMusicDisable, ingame_music_mp3)

            if Button(530, 555, self.exitButtonMenu, 1).draw(self.screen):
                self.state = GameState.EXIT
            
            # if Button(1207, 21, self.settingIcon, 1).draw(self.screen):
            #     if self.isOpenSetting:
            #         self.isOpenSetting = False
            #     else:
            #         self.isOpenSetting = True
            
            # if self.isOpenSetting:
            #     if self.isVolumeDisable:
            #         if Button(1207, 98, self.volumeDisableIcon, 1).draw(self.screen):
            #             self.isVolumeDisable = False
            #     else:
            #         if Button(1207, 98, self.volumeActiveIcon, 1).draw(self.screen):
            #             self.isVolumeDisable = True

            #     if (self.isMusicDisable and Button(1207, 175, self.musicDisableIcon, 1).draw(self.screen)) \
            #         or (not self.isMusicDisable and Button(1207, 175, self.musicActiveIcon, 1).draw(self.screen)):
            #             self.isMusicDisable = None#switchMusic(self.isMusicDisable)
                
            if Button(1200, 640, self.aboutUsButton, 0.5).draw(self.screen):
                webbrowser.open("https://drive.google.com/file/d/1njq8S15yb5eUZwvlXC8dDCMySusKQqPH/view?usp=sharing")
                # will change

        if self.state == GameState.PLAYING:
            if Button(1207, 21, self.settingIcon, 1).draw(self.screen):
                self.state = GameState.PAUSE
                  
        if self.state == GameState.PAUSE:
            self.screen.blit(self.settingTemplate, (375, 156))
            if Button(464, 248, self.resumeButton, 1).draw(self.screen):
                self.state = GameState.PLAYING
            if Button(464, 333, self.exitButtonSetting, 1).draw(self.screen):
                self.state = GameState.INIT
                self.ClearGame()
                self.screen.blit(self.logo, (363, 40))
                
                #playMusic(self.isMusicDisable, lobby_music_mp3)
            
            # if self.isVolumeDisable:
            #     if Button(532, 429, self.volumeDisableIcon, 1).draw(self.screen):
            #         self.isVolumeDisable = False
            # else:
            #     if Button(532, 429, self.volumeActiveIcon, 1).draw(self.screen):
            #         self.isVolumeDisable = True

            # if (self.isMusicDisable and Button(683, 429, self.musicDisableIcon, 1).draw(self.screen)) or (not self.isMusicDisable and Button(683, 429, self.musicActiveIcon, 1).draw(self.screen)):
            #         self.isMusicDisable = None#switchMusic(self.isMusicDisable)
            
        if self.state == GameState.END:
            self.endTemplate = pygame.transform.scale(self.settingTemplate, (int(self.settingTemplate.get_width() * 1.3), int(self.settingTemplate.get_height() * 1.3)))
            self.screen.blit(self.endTemplate, (300, 98))
            if Button(467, 517, self.homeButton, 1).draw(self.screen):
                self.state = GameState.INIT
                self.screen.blit(self.backgroundMainMenu, (0,0))
                self.screen.blit(self.logo, (363, 40))
                
                #playMusic(self.isMusicDisable, lobby_music_mp3)
            
            if Button(725, 517, self.restartButton, 1 ).draw(self.screen):
                self.state = GameState.PLAYING
                self.resetGame()

            if self.resultPlayer1 == Result.WIN:
                self.screen.blit(self.winIcon, (355,150))
                self.screen.blit(self.winImage, (370, 170))
            else:
                self.screen.blit(self.loseIcon, (355,150))
                self.screen.blit(self.loseImage, (370, 210))

            if self.resultPlayer2 == Result.WIN:
                self.screen.blit(self.winIcon, (700,150))
                self.screen.blit(self.winImage, (700, 170))
            else:
                self.screen.blit(self.loseIcon, (700,150))
                self.screen.blit(self.loseImage, (700, 210))

            

            
        if self.state == GameState.EXIT:
            pygame.quit()
            sys.exit()

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
        self.backgroundInGame = pygame.image.load("../asset/icon/Screen_InGame.png")
        self.backgroundMainMenu = pygame.image.load("../asset/icon/Screen_Lobby.png")
        self.logo = pygame.image.load("../asset/icon/asset/logo.png")
        self.playButton = pygame.image.load("../asset/icon/asset/play_button.png")
        self.exitButtonMenu = pygame.image.load("../asset/icon/asset/exit_button_menu.png")
        self.settingIcon = pygame.image.load("../asset/icon/asset/setting_icon.png")
        self.volumeActiveIcon = pygame.image.load("../asset/icon/asset/volume_active.png")
        self.volumeDisableIcon = pygame.image.load("../asset/icon/asset/volume_disable.png")
        self.musicActiveIcon = pygame.image.load("../asset/icon/asset/sound_active.png")
        self.musicDisableIcon = pygame.image.load("../asset/icon/asset/sound_disable.png")
        self.settingTemplate = pygame.image.load("../asset/icon/asset/setting_template.png")
        self.resumeButton = pygame.image.load("../asset/icon/asset/resume_button.png")
        self.exitButtonSetting = pygame.image.load("../asset/icon/asset/exit_button_setting.png")
        self.yesButton = pygame.image.load("../asset/icon/asset/yes_button.png")
        self.noButton = pygame.image.load("../asset/icon/asset/no_button.png")
        self.homeButton = pygame.image.load("../asset/icon/asset/home_button.png")
        self.restartButton = pygame.image.load("../asset/icon/asset/restart_button.png")
        self.aboutUsButton = pygame.image.load("../asset/icon/asset/aboutUs_button.png")
        self.exitPopupTemplate = pygame.image.load("../asset/icon/asset/exit_popup_template.png")
        self.winImage = pygame.image.load("../asset/icon/asset/WinImage.png")
        self.winIcon = pygame.image.load("../asset/icon/asset/WinIcon.png")
        self.loseImage = pygame.image.load("../asset/icon/asset/LoseImage.png")
        self.loseIcon = pygame.image.load("../asset/icon/asset/LoseIcon.png")
        #self.font = pygame.font.Font("../font/BalsamiqSans-Bold.ttf", 45)
        pygame.display.set_icon(icon)

        # Set icon for the game
        
        while True:
            self.HandleEventUI()
            #self.screen.fill((200,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                                        
            self.extraPlayers.Update(self.state,self.screen,self.bulletManager,10)
            self.mainPlayers.Update(self.state,self.screen,self.bulletManager,10)
            if self.state == GameState.PLAYING:
                self.edgeManager.draw(self.screen)
                self.bulletManager.moveAllBullet(self.screen, self.edgeManager)
            if self.state == GameState.PLAYING:
                if self.mainPlayers.players.__len__() == 0 or self.extraPlayers.players.__len__() == 0:
                    self.endGame()
            self.CheckBulletCollision()
            self.clock.tick(FPS)
            pygame.display.update()

    def endGame(self):
        self.state = GameState.END
    def ClearGame(self):
        self.mainPlayers.players.clear()
        self.extraPlayers.players.clear()
        self.bulletManager.bulletList.clear()
        
    def resetGame(self):
        self.ClearGame()
        self.InitGame()
        self.state = GameState.PLAYING
    def CheckBulletCollision(self):
        for bullet in self.bulletManager.bulletList:
            for player in self.mainPlayers.players:
                if player.hit(bullet):
                    print("Main player hit bullet")
                    if self.mainPlayers.players.__len__() - 1 != 0 and player == self.mainPlayers.currentPlayer:
                        self.mainPlayers.SwitchPlayer()
                    self.mainPlayers.RemovePlayer(player)
                    self.bulletManager.removeBullet(bullet)
            for player in self.extraPlayers.players:
            
                if player.hit(bullet):
                    if self.extraPlayers.players.__len__() -1 != 0 and player == self.extraPlayers.currentPlayer:
                        self.extraPlayers.SwitchPlayer()
                    self.extraPlayers.RemovePlayer(player)
                    self.bulletManager.removeBullet(bullet)
                    print("Extra player hit bullet")

