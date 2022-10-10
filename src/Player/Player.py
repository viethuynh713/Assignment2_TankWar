

import math
import pygame

from EnumClass import PlayerType

vector2 = pygame.math.Vector2
class Player(pygame.sprite.Sprite):
    def __init__(self, pos: vector2, dir: vector2, isMain):
        self.position = pos
        self.rootDir = dir
        self.direction = dir
        self.SPEED = 10
        self.DENTAL_ANGLE = 1
        self.CalculateAngle()
        if isMain == PlayerType.MAIN:
            self.rootImage = pygame.image.load('../asset/Image/player.png')
        else:
            self.rootImage = pygame.image.load('../asset/Image/extraPlayer.png')
        self.rootImage = pygame.transform.scale(self.rootImage,(70,70))
        self.rect = self.rootImage.get_rect()
        self.rect.center = 35,35
        
        self.image,self.rect = self.rot_center(self.rootImage,self.rect,self.angle)

    def CalculateAngle(self):
        self.angle = vector2.angle_to(self.direction, vector2(0,-1))

    def move(self, up: bool):
        if up:
            self.position += self.direction*self.SPEED
        else:
            self.position -= self.direction*self.SPEED
        
        if(self.position.x < 0):self.position.x = 0
        if(self.position.x > 1210):self.position.x = 1210
        if(self.position.y < 0):self.position.y = 0
        if(self.position.y > 650):self.position.y = 650

    def rotate(self, clockwise: bool):
        if clockwise:
            self.angle += self.DENTAL_ANGLE
            #self.direction = vector2.rotate(self.direction,self.DENTAL_ANGLE)
            # self.image = pygame.transform.rotate(self.image, -self.DENTAL_ANGLE)
        else:
            self.angle -= self.DENTAL_ANGLE
            #self.direction = vector2.rotate(self.direction,-self.DENTAL_ANGLE)
            # self.image = pygame.transform.rotate(self.image, self.DENTAL_ANGLE)
        self.image,self.rect = self.rot_center(self.rootImage,self.rect,self.angle)
        self.direction = vector2.rotate(self.rootDir,self.angle + 90)
        #self.image = pygame.transform.rotate(self.image, self.angle)
        

    def rot_center(self,image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
    def update(self,screen):
        pygame.draw.rect(screen,(0,200,200),self.rect)
        screen.blit(self.image,self.position)
        
    def fire(self):
        return self.position,self.direction

    def hit(self,image):
        pass
