import pygame
from inputmanager import *
from gamemanager import *
from playerbullet import *

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("resources/player.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x - self.image.get_width() / 2,
                                 self.y - self.image.get_height()/ 2))

    def run(self):
        if input_manager.right_pressed:
            self.x += 20
        if input_manager.left_pressed:
            self.x -= 20
        if input_manager.up_pressed:
            self.y -= 20
        if input_manager.down_pressed:
            self.y += 20
        if input_manager.space_pressed:
            player_bullet = PlayerBullet()
            player_bullet.x = self.x
            player_bullet.y = self.y - 20
            game_manager.add(player_bullet)