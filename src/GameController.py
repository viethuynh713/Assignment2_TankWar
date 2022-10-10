import sys
import pygame
from pygame.locals import *
from Button import *
import webbrowser
from enum import Enum
import random
import math

from Constant import *

class State(Enum):
    INIT = 0,
    PLAYING = 1,
    PAUSE = 2,
    END = 3,
    EXITGAME = 4;

class Result(Enum):
    LOSE = 0,
    WIN = 1;


class GameController():
    def __init__(self):
        self.state = State.END
        self.isOpenSetting = False
        self.isMusicDisable = False
        self.isVolumeDisable = False
        self.resultPlayer1 = Result.LOSE
        self.resultPlayer2 = Result.WIN
        self.Play()
    def InitGame(self):
        pass

    def HandleEventUI(self):
        #self.screen.blit(self.background, (0, 0))
        if self.state == State.INIT:
            # TODO: Draw panel game
            self.screen.blit(self.backgroundMainMenu, (0,0))
            self.screen.blit(self.logo, (363, 40))

            if Button(530, 355, self.playButton, 1).draw(self.screen):
                self.isOpenSetting = False
                self.state = State.PLAYING
                #playMusic(self.isMusicDisable, ingame_music_mp3)

            if Button(530, 555, self.exitButtonMenu, 1).draw(self.screen):
                self.state = State.EXITGAME
            
            if Button(1207, 21, self.settingIcon, 1).draw(self.screen):
                if self.isOpenSetting:
                    self.isOpenSetting = False
                else:
                    self.isOpenSetting = True
            
            if self.isOpenSetting:
                if self.isVolumeDisable:
                    if Button(1207, 98, self.volumeDisableIcon, 1).draw(self.screen):
                        self.isVolumeDisable = False
                else:
                    if Button(1207, 98, self.volumeActiveIcon, 1).draw(self.screen):
                        self.isVolumeDisable = True

                if (self.isMusicDisable and Button(1207, 175, self.musicDisableIcon, 1).draw(self.screen)) \
                    or (not self.isMusicDisable and Button(1207, 175, self.musicActiveIcon, 1).draw(self.screen)):
                        self.isMusicDisable = None#switchMusic(self.isMusicDisable)
                
            if Button(1200, 640, self.aboutUsButton, 0.5).draw(self.screen):
                webbrowser.open("https://drive.google.com/file/d/1njq8S15yb5eUZwvlXC8dDCMySusKQqPH/view?usp=sharing")
                # will change

        if self.state == State.PLAYING:
            self.screen.blit(self.backgroundInGame, (0,0))
            if Button(1207, 21, self.settingIcon, 1).draw(self.screen):
                self.state = State.PAUSE
                  
        if self.state == State.PAUSE:
            self.screen.blit(self.settingTemplate, (375, 156))
            if Button(464, 248, self.resumeButton, 1).draw(self.screen):
                self.state = State.PLAYING
            if Button(464, 333, self.exitButtonSetting, 1).draw(self.screen):
                self.state = State.INIT
                self.screen.blit(self.backgroundMainMenu, (0,0))
                self.screen.blit(self.logo, (363, 40))
                
                #playMusic(self.isMusicDisable, lobby_music_mp3)
            
            if self.isVolumeDisable:
                if Button(532, 429, self.volumeDisableIcon, 1).draw(self.screen):
                    self.isVolumeDisable = False
            else:
                if Button(532, 429, self.volumeActiveIcon, 1).draw(self.screen):
                    self.isVolumeDisable = True

            if (self.isMusicDisable and Button(683, 429, self.musicDisableIcon, 1).draw(self.screen)) or (not self.isMusicDisable and Button(683, 429, self.musicActiveIcon, 1).draw(self.screen)):
                    self.isMusicDisable = None#switchMusic(self.isMusicDisable)
            
        if self.state == State.END:
            self.screen.blit(self.backgroundInGame, (0,0))
            self.endTemplate = pygame.transform.scale(self.settingTemplate, (int(self.settingTemplate.get_width() * 1.3), int(self.settingTemplate.get_height() * 1.3)))
            self.screen.blit(self.endTemplate, (300, 98))
            if Button(467, 517, self.homeButton, 1).draw(self.screen):
                self.state = State.INIT
                self.screen.blit(self.backgroundMainMenu, (0,0))
                self.screen.blit(self.logo, (363, 40))
                
                #playMusic(self.isMusicDisable, lobby_music_mp3)
            
            if Button(725, 517, self.restartButton, 1 ).draw(self.screen):
                self.state = State.PLAYING
                self.InitGame()

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

            

            
        if self.state == State.EXITGAME:
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
            #self.screen.blit(background, (0,0))
            self.HandleEventUI()
            print(self.state)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    def endGame(self):
        pass
    def resetGame(self):
        pass