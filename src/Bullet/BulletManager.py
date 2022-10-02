import pygame, sys
from pygame.locals import *

from Bullet.Bullet import Bullet


class BulletManager:
    def __init__(self) -> None:
        self.bulletList = []

    def createBullet(self, pos: tuple, direction: float) -> None:
        bullet = Bullet(pos, direction)
        self.bulletList.append(bullet)

    def removeBullet(self, bullet: Bullet) -> None:
        self.bulletList.remove(bullet)

    def draw(self, surface) -> None:
        for bullet in self.bulletList:
            bullet.move()
            bullet.draw(surface)