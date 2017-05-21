import pygame
from inputmanager import *

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("resources/player.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def run(self):
        if input_manager.right_pressed:
            self.x += 10
        if input_manager.left_pressed:
            self.x -= 10
        if input_manager.up_pressed:
            self.y -= 10
        if input_manager.down_pressed:
            self.y += 10