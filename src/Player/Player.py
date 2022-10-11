

import math
import pygame

from EnumClass import PlayerType
from Wall.EdgeManager import EdgeManager

vector2 = pygame.math.Vector2
class Player(pygame.sprite.Sprite):
    def __init__(self, pos: vector2, dir: vector2, isMain):
        self.position = pos
        self.rootDir = vector2(0,-1)
        self.SPEED = 10
        self.DENTAL_ANGLE = 1
        self.direction = dir
        self.CalculateAngle()
        if isMain == PlayerType.MAIN:
            self.rootImage = pygame.image.load('../asset/Image/player.png')
        else:
            self.rootImage = pygame.image.load('../asset/Image/extraPlayer.png')
        self.rootImage = pygame.transform.scale(self.rootImage,(50,50))
        self.rect = self.rootImage.get_rect()
        self.rect.center = pos + vector2(25,25)
        self.image,self.rect = self.rot_center(self.rootImage,self.rect,self.angle)

    def CalculateAngle(self):
        self.angle = vector2.angle_to(self.direction, vector2(0,-1))

    def move(self, up: bool, edgeManager: EdgeManager):
        if up:
            self.position += self.direction*self.SPEED
            if edgeManager.checkCollidePlayer(self.rect):
                self.position -= self.direction*self.SPEED
        else:
            self.position -= self.direction*self.SPEED
            if edgeManager.checkCollidePlayer(self.rect):
                self.position += self.direction*self.SPEED
        
        if(self.position.x < 0):self.position.x = 0
        if(self.position.x > 1210):self.position.x = 1210
        if(self.position.y < 0):self.position.y = 0
        if(self.position.y > 650):self.position.y = 650
        self.rect.center = self.position + vector2(25,25)
        
        if edgeManager.checkCollidePlayer(self.rect):
            if up:
                self.position -= self.direction*self.SPEED
            else:
                self.position += self.direction*self.SPEED
        
        if(self.position.x < 0):self.position.x = 0
        if(self.position.x > 1210):self.position.x = 1210
        if(self.position.y < 0):self.position.y = 0
        if(self.position.y > 650):self.position.y = 650
        self.rect.center = self.position + vector2(25,25)


    def rotate(self, clockwise: bool, edgeManager: EdgeManager):
        if clockwise:
            self.angle += self.DENTAL_ANGLE
            if edgeManager.checkCollidePlayer(self.rect):
                self.angle -= self.DENTAL_ANGLE
        else:
            self.angle -= self.DENTAL_ANGLE
            if edgeManager.checkCollidePlayer(self.rect):
                self.angle += self.DENTAL_ANGLE
            
        self.image,self.rect = self.rot_center(self.rootImage,self.rect,self.angle)
        temDirection = vector2.rotate(self.rootDir,self.angle + 180)
        self.direction = vector2(temDirection.x,-temDirection.y)
        #print(self.angle ,"--", self.direction)
        
        if edgeManager.checkCollidePlayer(self.rect):
            if clockwise:
                self.angle -= self.DENTAL_ANGLE
            else:
                self.angle += self.DENTAL_ANGLE
            
        self.image,self.rect = self.rot_center(self.rootImage,self.rect,self.angle)
        temDirection = vector2.rotate(self.rootDir,self.angle + 180)
        self.direction = vector2(temDirection.x,-temDirection.y)
        

    def rot_center(self,image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
    def update(self,screen):
        
        
        # pygame.draw.rect(screen,(0,200,200),self.rect)
        screen.blit(self.image,self.position)
        
    def fire(self):
        return self.rect.center + self.direction*60,self.direction

    def hit(self,bullet):
        if self.rect.collidepoint(bullet.pos):
            return True
        return False
