import pygame
from Bullet.BulletManager import BulletManager
from Constant import TIME_FIRE, TIME_SWITCH
from EnumClass import GameState, PlayerType
from Player.Player import Player

from pygame.locals import *

from Wall.EdgeManager import EdgeManager
vector2 = pygame.math.Vector2
class PlayerManager:
    def __init__(self, typeOfPlayer:PlayerType, edgeManager: EdgeManager):
        self.edgeManager = edgeManager
        self.players = []
        self.canFire = True
        self.CanSwitch = True
        self.TimeFire = 3000
        self.TimeSwitch = 1000
        self.playerType = typeOfPlayer
        self.flag = pygame.image.load('../asset/icon/flag.png')
        #self.flag = pygame.transform.scale(self.flag,(30,30))
        
    def InitOnePlayer(self,pos:vector2):
        dir = vector2()
        if self.playerType == PlayerType.MAIN:
            dir = vector2(1,0)
        else:
            dir = vector2(-1,0)
            
        self.players.append(Player(pos,dir, self.playerType))
        
        self.currentPlayer = self.players[0]
        
    def HitPlayer(self,pos : tuple):
        pass
    def RemovePlayer(self,player:Player):
        self.players.remove(player)
        
    def SwitchPlayer(self):
        index = self.players.index(self.currentPlayer)
        if index < self.players.__len__() -1:
            self.currentPlayer = self.players[index + 1] 
        else:
            self.currentPlayer = self.players[0]
    def CountDownFire(self,dt):
        self.TimeFire -= dt
        self.TimeSwitch -= dt
        if self.TimeFire <= 0:
            self.canFire = True
            self.TimeFire = TIME_FIRE
        if self.TimeSwitch <= 0:
            self.CanSwitch = True
            self.TimeSwitch = TIME_SWITCH
    def Update(self,state,screen,bulletManager:BulletManager,dt):
        press = pygame.key.get_pressed()
       
        self.CountDownFire(dt)
        if state == GameState.PLAYING:
            if self.playerType == PlayerType.MAIN:
                if press[pygame.K_a]:
                    self.currentPlayer.rotate(True, self.edgeManager)
                if press[pygame.K_d]:
                    self.currentPlayer.rotate(False, self.edgeManager)
                if press[pygame.K_w]:
                    self.currentPlayer.move(True, self.edgeManager)
                if press[pygame.K_s]:
                    self.currentPlayer.move(False, self.edgeManager)
                if press[pygame.K_v]and self.CanSwitch:
                    self.SwitchPlayer()
                    self.CanSwitch = False
                if press[pygame.K_b] and self.canFire:
                    pos,dir = self.currentPlayer.fire()
                    bulletManager.createBullet(pos,dir)
                    self.canFire = False
                    
            else:
                if press[pygame.K_LEFT]:
                    self.currentPlayer.rotate(True, self.edgeManager)
                if press[pygame.K_RIGHT]:
                    self.currentPlayer.rotate(False, self.edgeManager)
                if press[pygame.K_UP]:
                    self.currentPlayer.move(True, self.edgeManager)
                if press[pygame.K_DOWN]:
                    self.currentPlayer.move(False, self.edgeManager)
                if press[pygame.K_n] and self.CanSwitch:
                    self.SwitchPlayer()
                    self.CanSwitch =False
                if press[pygame.K_m]and self.canFire:
                    pos,dir = self.currentPlayer.fire()
                    bulletManager.createBullet(pos,dir)
                    self.canFire = False
            screen.blit(self.flag,(self.currentPlayer.position.x - 45,self.currentPlayer.position.y - 45))
            for player in self.players:
                player.update(screen)
                
            
            
        
    