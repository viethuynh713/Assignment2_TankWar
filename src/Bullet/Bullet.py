import pygame, sys
from pygame.locals import *
from Constant import *
from pygame.math import *

class Bullet:
    def __init__(self, bulletManager, pos: Vector2, direction: Vector2) -> None:
        self.bulletManager = bulletManager
        self.pos = pos
        self.prevPos = self.pos.copy()
        self.speed = BULLET_SPEED_INIT
        self.direction = direction
        self.restTime = REST_TIME_INIT

    def move(self) -> None:
        if self.restTime == 0:
            self.bulletManager.removeBullet(self)
            return
        self.prevPos = self.pos.copy()
        self.pos += self.direction * self.speed
        self.restTime -= 1

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, (0, 0, 255), self.pos, 5)