import pygame
import random

class Ball:
    def __init__(self, radius, screen, initial_speed):
        self.radius = radius
        self.screen = screen
        self.speed_x, self.speed_y = initial_speed + 1, initial_speed
        self.color = "#FFFFFF"
    
        self.init_movement()
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    
    def init_movement(self):
        self.x = (self.screen.get_width()/2) - (self.radius/2)
        self.y = (self.screen.get_height()/2) - (self.radius/2)
    
    def move(self):
        self.x -= self.speed_x
        self.y -= self.speed_y
        if 0 > self.y:
            self.speed_y *= -1
        if self.screen.get_height() < self.y:
            self.speed_y *= -1
    