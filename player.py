from sys import winver
import pygame
import os
from main import WIN, HEIGHT, WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT, DEFAULT_PLAYER_X, DEFAULT_PLAYER_Y


camera = pygame.Rect(0, 0, WIDTH, HEIGHT)
PLAYER_SRC = pygame.image.load(os.path.join('Assets', 'player.png'))

PLAYER_L = pygame.transform.scale(PLAYER_SRC.subsurface(65, 27, 63, 163), (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_R = pygame.transform.scale(PLAYER_SRC.subsurface(292, 27, 63, 163), (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_U = pygame.transform.scale(PLAYER_SRC.subsurface(391, 27, 90, 163), (3/2*PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_D = pygame.transform.scale(PLAYER_SRC.subsurface(161, 27, 90, 163), (3/2*PLAYER_WIDTH, PLAYER_HEIGHT))

class Player:    
    def __init__(self):
        self.win = WIN
        self.x = DEFAULT_PLAYER_X
        self.y = DEFAULT_PLAYER_Y
        self.direction = 'S'
    def draw(self):
        if self.direction == 'L':
            self.win.blit(PLAYER_L, (self.x, self.y))
        elif self.direction == 'R':
            self.win.blit(PLAYER_R, (self.x, self.y))
        elif self.direction == 'U':
            self.win.blit(PLAYER_U, (self.x, self.y))
        else:
            self.win.blit(PLAYER_D, (self.x, self.y))  


    def movement(self, camera, camera_x_left_locked, camera_x_right_locked, camera_y_left_locked, camera_y_right_locked):

        direction = '' 
        x, y = 0, 0

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            y -= 8
            self.direction = 'U'
        if keys_pressed[pygame.K_s]:
            y += 8
            self.direction = 'D'
        if keys_pressed[pygame.K_a]:
            x -= 8
            self.direction = 'R'
        if keys_pressed[pygame.K_d]:
            x += 8
            self.direction = 'L'
        self.draw()
        #print(self.x, camera_x_right_locked)
        if self.x + PLAYER_WIDTH/2 == WIDTH/2:
            camera_x_locked = True

        else: 
            camera_x_locked = False
        if   self.y + PLAYER_HEIGHT/2 == HEIGHT/2:
            camera_y_locked = True   
        else: 
            camera_y_locked = False


        if camera_x_locked: 
            if x<0 and not camera_x_left_locked:
                self.x += x
            elif x>0 and not camera_x_right_locked:
                self.x += x
            else:
                camera.x += x
        elif not camera_x_locked: 
            self.x += x
        if camera_y_locked: 
            if y<0 and not camera_y_left_locked:
                self.y += y
            elif y>0 and not camera_y_right_locked:
                self.y += y
            else:
                camera.y += y
        elif not camera_y_locked: 
            self.y += y  
        

