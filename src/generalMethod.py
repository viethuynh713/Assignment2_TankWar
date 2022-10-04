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
    a = pos1.y - pos2.y
    b = pos2.x - pos1.x
    c = -pos1.x * a - pos1.y * b
    return (a, b, c)

def isPointInLine(line: tuple[Vector2, Vector2], point: Vector2) -> bool:
    if (point.x >= line[0].x and point.x <= line[1].x) or (point.x >= line[1].x and point.x <= line[0].x):
        return True
    return False

def cutPointOf2Lines(line1: tuple[Vector2, Vector2], line2: tuple[Vector2, Vector2]) -> Vector2:
    a1, b1, c1 = lineEquation(line1[0], line1[1])
    a2, b2, c2 = lineEquation(line2[0], line2[1])
    if a1 == None or a2 == None:
        return None
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([-c1, -c2])
    cutPntx, cutPnty = solveSystemEquations(A, B)
    cutPnt = Vector2(cutPntx, cutPnty)
    if isPointInLine(line1, cutPnt) and isPointInLine(line2, cutPnt):
        print(str(cutPnt))
        return cutPnt
    return None

def perpendicularProjectPointToLine(line: tuple[Vector2, Vector2], point: Vector2) -> Vector2:
    a = Vector2.normalize(line[1] - line[0])
    b = point - line[0]
    c = a * b
    return line[0] + c * a

def symmetryPointThroughLine(line: tuple[Vector2, Vector2], point: Vector2) -> Vector2:
    x0, y0 = perpendicularProjectPointToLine(line, point)
    x = x0 + (x0 - point.x)
    y = y0 + (y0 - point.y)
    return Vector2(x, y)

def reflectVector(velocity: Vector2, normalize: Vector2) -> Vector2:
    # print(str(velocity) + ", " + str(normalize))
    angle = abs(Vector2.angle_to(velocity, normalize))
    print(angle)
    n = normalize.copy()
    if angle < 90:
        n = -n
    return velocity - 2 * n * (velocity * n)