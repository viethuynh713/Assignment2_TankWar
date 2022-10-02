from pygame.math import *

def linearCoefficient(pos1: Vector2, pos2: Vector2) -> tuple[float, float]:
    a = (pos1.y - pos2.y) / (pos1.x - pos2.x)
    b = pos1.y - a * pos1.x
    return (a, b)

def isPointInLine(line: tuple(Vector2, Vector2), point: Vector2) -> bool:
    if (point.x >= line[0].x and point.x <= line[1].x) \
        or (point.x >= line[1].x and point.x <= line[0].x):
        return True
    return False

def cutPointOf2Lines(line1: tuple(Vector2, Vector2), line2: tuple(Vector2, Vector2)) -> Vector2:
    a1, b1 = linearCoefficient(line1[0], line1[1])
    a2, b2 = linearCoefficient(line2[0], line2[1])
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    cutPnt = Vector2(x, y)
    if isPointInLine(line1, cutPnt) and isPointInLine(line2, cutPnt):
        return cutPnt
    return None

def perpendicularProjectPointToLine(line: tuple(Vector2, Vector2), point: Vector2) -> Vector2:
    a, b = linearCoefficient(line[0], line[1])
    x = ((line[0].x - line[1].x) * point.x + (line[0].y - line[1].y) * (point.y - b)) \
        / ((line[0].x - line[1].x) + a * (line[0].y - line[1].y))
    y = a * x + b
    return (x, y)

def symmetryPointThroughLine(line: tuple(Vector2, Vector2), point: Vector2) -> Vector2:
    x0, y0 = perpendicularProjectPointToLine(line, point)
    x = x0 + (x0 - point.x)
    y = y0 + (y0 - point.y)
    return (x, y)

def reflectVector(velocity: Vector2, normalize: Vector2) -> Vector2:
    return velocity - 2 * normalize * (velocity * normalize)