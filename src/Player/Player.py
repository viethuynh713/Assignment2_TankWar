

import math
import pygame

vector2 = pygame.math.Vector2
class Player(pygame.sprite.Sprite):
    def __init__(self, pos: vector2, dir: vector2):
        self.position = pos
        self.direction = dir
        self.SPEED = 1
        self.DENTAL_ANGLE = 0.1
        self.CalculateAngle()
        self.image = pygame.image.load('../asset/Image/player.png')
        self.image = pygame.transform.scale(self.image,(70,70))
        self.image = pygame.transform.rotate(self.image, self.angle)

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
            self.angle -= self.DENTAL_ANGLE
            self.direction = vector2.rotate(self.direction,- self.DENTAL_ANGLE)
            self.image = pygame.transform.rotate(self.image, -self.DENTAL_ANGLE)
        else:
            self.angle += self.DENTAL_ANGLE
            self.direction = vector2.rotate(self.direction,self.DENTAL_ANGLE)
            self.image = pygame.transform.rotate(self.image, self.DENTAL_ANGLE)
            
        #self.image = pygame.transform.rotate(self.image, self.angle)
        

    def update(self,screen):
        screen.blit(self.image,self.position)
        
    def fire():
        pass

    def hit():
        pass
