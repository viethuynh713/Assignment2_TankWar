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

    def checkBounce(self, pos: Vector2, prevPos: Vector2, direction: Vector2) -> tuple[Vector2, Vector2]:
        posRes, dirRes = (pos, direction)
        cutPointRes, edgeRes = (None, None)
        for edge in self.edgeList:
            cutPointTemp, edgeTemp = edge.checkBounce(pos, prevPos)
            if cutPointTemp != None:
                #print(str(prevPos) + ", " + str(pos))
                if cutPointRes == None:
                    cutPointRes, edgeRes = (cutPointTemp, edgeTemp)
                elif abs(cutPointTemp.x - pos.x) < abs(cutPointRes.x - pos.x):
                    cutPointRes, edgeRes = (cutPointTemp, edgeTemp)
        if cutPointRes != None:
            posRes = symmetryPointThroughLine(edgeRes.getEdge(), pos)
            dirRes = reflectVector(direction, edgeRes.getNormalize())
        return (posRes, dirRes)

    def draw(self, screen):
        for edge in self.edgeList:
            edge.draw(screen)