import pygame, sys
from pygame.locals import *
from pygame.math import *
from generalMethod import *

from Constant import EDGE_FRICTION

class Edge:
    def __init__(self, pos1: Vector2, pos2: Vector2) -> None:
        self.edge = (pos1, pos2)
        self.friction = EDGE_FRICTION
        # support statistics
        self.normalize = Vector2.normalize(Vector2.rotate(pos2 - pos1, 90))
        self.a, self.b = linearCoefficient(self.edge[0], self.edge[1])

    def checkBounce(self, pos: Vector2, prevPos: Vector2) -> tuple:
        return (cutPointOf2Lines(self.edge, (prevPos, pos)), self)

    def draw(self, screen):
        pygame.draw.line(screen, (48, 213, 200), self.edge[0], self.edge[1], 3)

    def getEdge(self):
        return self.edge

    def getNormalize(self):
        return self.normalize