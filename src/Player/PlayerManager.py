
import pygame
from Bullet.BulletManager import BulletManager
from EnumClass import GameState, PlayerType
from Player.Player import Player

from pygame.locals import *
vector2 = pygame.math.Vector2
class PlayerManager:
    def __init__(self,typeOfPlayer:PlayerType):
        self.players = []
        
        self.playerType = typeOfPlayer
        self.flag = pygame.image.load('../asset/icon/flag.png')
        self.flag = pygame.transform.scale(self.flag,(20,20))
        
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
    def Update(self,state,screen,bulletManager:BulletManager):
        press = pygame.key.get_pressed()
        
        if state == GameState.PLAYING:
            if self.playerType == PlayerType.MAIN:
                if press[pygame.K_a]:
                    self.currentPlayer.rotate(True)
                if press[pygame.K_d]:
                    self.currentPlayer.rotate(False)
                if press[pygame.K_w]:
                    self.currentPlayer.move(True)
                if press[pygame.K_s]:
                    self.currentPlayer.move(False)
                if press[pygame.K_v]:
                    self.SwitchPlayer()
                if press[pygame.K_b]:
                    pos,dir = self.currentPlayer.fire()
                    #print(pos,"//",dir)
                    bulletManager.createBullet(pos,dir)
            else:
                if press[pygame.K_LEFT]:
                    self.currentPlayer.rotate(True)
                if press[pygame.K_RIGHT]:
                    self.currentPlayer.rotate(False)
                if press[pygame.K_UP]:
                    self.currentPlayer.move(True)
                if press[pygame.K_DOWN]:
                    self.currentPlayer.move(False)
                if press[pygame.K_n]:
                    self.SwitchPlayer()
                if press[pygame.K_m]:
                    pos,dir = self.currentPlayer.fire()
                    bulletManager.createBullet(pos,dir)
        for player in self.players:
            player.update(screen)
        screen.blit(self.flag,(self.currentPlayer.position.x,self.currentPlayer.position.y))
            
        
    