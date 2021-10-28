import pygame
import os
from main import WIN
from player import x, y 

MONSTER_WIDTH, MONSTER_HEIGHT = 75, 90

MONSTER_SRC = pygame.image.load(os.path.join('Assets', 'monster.png'))
MONSTER = pygame.transform.scale(MONSTER_SRC, (MONSTER_WIDTH, MONSTER_HEIGHT))


class Monster():
    def __init__(self):
        self.x = 800
        self.y = 400
        
    def move(self, camera):
        global x, y
        self.x -= camera.delta_x
        self.y -= camera.delta_y
        print(camera.delta_x, camera.delta_y)
        camera.delta_x = 0
        camera.delta_y = 0
    def draw(self):
        WIN.blit(MONSTER, (self.x, self.y))