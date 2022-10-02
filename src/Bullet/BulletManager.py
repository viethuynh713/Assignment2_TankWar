import pygame, sys
from pygame.locals import *
from pygame.math import *

from Bullet.Bullet import *


class BulletManager:
    def __init__(self) -> None:
        self.bulletList = []

    def createBullet(self, pos: Vector2, direction: Vector2) -> None:
        bullet = Bullet(self, pos, direction)
        self.bulletList.append(bullet)

    def removeBullet(self, bullet: Bullet) -> None:
        self.bulletList.remove(bullet)

    def moveAllBullet(self, screen) -> None:
        for bullet in self.bulletList:
            bullet.move()
            bullet.draw(screen)