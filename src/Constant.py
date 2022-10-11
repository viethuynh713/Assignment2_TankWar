from pygame.math import *

HEIGHT_SCREEN = 720
WIDTH_SCREEN = 1280
FPS = 30

UNIT_VECTOR = Vector2(1, 0)
BULLET_SPEED_INIT = 150 / FPS
REST_TIME_INIT = 20000 * FPS
EDGE_FRICTION = 9 / FPS
TIME_FIRE = 3000
TIME_SWITCH = 1000