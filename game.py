import pygame
import os
import random

assets_path = os.path.join(os.path.dirname(__file__), 'assets')


class Background(pygame.sprite.Sprite):
    number = random.randint(1, 3)

    def __init__(self, scroll_speed, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(assets_path, 'background', f'background_{Background.number}.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scroll_speed = scroll_speed

    def update(self):
        self.rect.y += self.scroll_speed
        win_height = pygame.display.get_surface().get_height()

        if self.rect.y >= win_height:
            self.rect.y = -(self.image.get_height() + self.image.get_height() - win_height)
            print(1)


class Player(pygame.sprite.Sprite):
    # Todo add more featres to the player class
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(assets_path, 'player', 'ship.png'))
        self.image = pygame.transform.scale2x(self.image)
        self.position = [x, y]

    def draw(self, screen):
        screen.blit(self.image, (self.position[0], self.position[1]))