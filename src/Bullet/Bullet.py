import pygame, sys
from pygame.locals import *
from Constant import *
from pygame.math import *


class Bullet:
    def __init__(self, pos: Vector2, direction: Vector2) -> None:
        self.pos = pos
        self.speed = BULLET_SPEED_INIT
        self.direction = direction
        self.restTime = REST_TIME_INIT

    def move(self) -> None:
        self.pos += self.direction

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, (0, 255, 0), self.pos, 5)