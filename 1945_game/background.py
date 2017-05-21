import pygame

class Background:
    def __init__(self):
        self.image = pygame.image.load("resources/background.png")
        self.y = 0
        self.y2 = -self.image.get_height()

    def draw(self, screen):
        screen.blit(self.image, (0, self.y))
        screen.blit(self.image, (0, self.y2))

    def run(self):
        pass