from pygame.math import *
import numpy as np

def solveSystemEquations(A: np.array, B: np.array) -> np.array:
    res = None
    try:
        res = np.linalg.inv(A).dot(B)
    except:
        res = []
        for i in range(len(B)):
            res.append(None)
        return np.array(res)
    else:
        return res

def lineEquation(pos1: Vector2, pos2: Vector2) -> tuple:
    A = np.array([[pos1.x, pos1.y, 1], [pos2.x, pos2.y, 1], [pos1.y - pos2.y, pos1.x - pos2.x, 0]])
    B = np.array([0, 0, 0])
    return tuple(solveSystemEquations(A, B))

def isPointInLine(line: tuple[Vector2, Vector2], point: Vector2) -> bool:
    if (point.x >= line[0].x and point.x <= line[1].x) \
        or (point.x >= line[1].x and point.x <= line[0].x):
        return True
    return False

def cutPointOf2Lines(line1: tuple[Vector2, Vector2], line2: tuple[Vector2, Vector2]) -> Vector2:
    a1, b1, c1 = lineEquation(line1[0], line1[1])
    a2, b2, c2 = lineEquation(line2[0], line2[1])
    if a1 == None or a2 == None:
        return None
    A = np.array([a1, b1], [a2, b2])
    B = np.array([-c1, -c2])
    cutPnt = solveSystemEquations(A, B)
    if isPointInLine(line1, cutPnt) and isPointInLine(line2, cutPnt):
        return cutPnt
    return None

def perpendicularProjectPointToLine(line: tuple[Vector2, Vector2], point: Vector2) -> Vector2:
    a, b = linearCoefficient(line[0], line[1])
    x = ((line[0].x - line[1].x) * point.x + (line[0].y - line[1].y) * (point.y - b)) \
        / ((line[0].x - line[1].x) + a * (line[0].y - line[1].y))
    y = a * x + b
    return (x, y)

def symmetryPointThroughLine(line: tuple[Vector2, Vector2], point: Vector2) -> Vector2:
    x0, y0 = perpendicularProjectPointToLine(line, point)
    x = x0 + (x0 - point.x)
    y = y0 + (y0 - point.y)
    return (x, y)

def reflectVector(velocity: Vector2, normalize: Vector2) -> Vector2:
    return velocity - 2 * normalize * (velocity * normalize)