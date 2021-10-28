import pygame


class Camera():
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.delta_x = 0
        self.delta_y = 0
        self.camera_x_right_locked = True 
        self.camera_x_left_locked = True
        self.camera_y_right_locked = True
        self.camera_y_left_locked = True 
    def check(self):
        
       #print(self.x, self.y, self.camera_x_left_locked, self.camera_y_right_locked, self.camera_y_left_locked, self.camera_x_right_locked)
        pass