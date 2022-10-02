import pygame, sys
from pygame.locals import *
from pygame.math import *

from Wall.Edge import Edge
from generalMethod import reflectVector, symmetryPointThroughLine

class EdgeManager:
    def __init__(self) -> None:
        self.edgeList = []

    def createEdge(self, pos1: Vector2, pos2: Vector2) -> None:
        edge = Edge(pos1, pos2)
        self.edgeList.append(edge)

    def checkBounce(self, pos: Vector2, prevPos: Vector2, speed: Vector2) -> tuple[Vector2, Vector2]:
        pos, direction = (None, None)
        cutPoint, edge = (None, None)
        for edge in self.edgeList:
            cutPointTemp, edgeTemp = edge.checkBounce(pos, prevPos)
            if cutPointTemp != None:
                if cutPoint != None:
                    cutPoint, edge = (cutPointTemp, edgeTemp)
                elif abs(cutPointTemp.x - pos.x) < abs(cutPoint.x - pos.x):
                    cutPoint, edge = (cutPointTemp, edgeTemp)
        if cutPoint != None:
            pos = symmetryPointThroughLine(edge.getEdge(), pos)
            direction = reflectVector(speed, edge.getNormalize())
        return (pos, direction)

    def draw(self, screen):
        for edge in self.edgeList:
            edge.draw(screen)