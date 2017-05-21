import pygame
from gamemanager import *

class EnemyPlane:
    def __init__(self):
        self.x = 250
        self.y = 0
        self.x1 = 150
        self.y2 = 0
        self.image = pygame.image.load("resources/enemy_plane.png")
        self.image1 = pygame.image.load("resources/enemy_plane_1.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image1,(self.x1, self.y2))
    def run(self):
        self.y += 3
        self.y2 += 2