import pygame
import os
import random
import time

assets_path = os.path.join(os.path.dirname(__file__), 'assets')


class Background(pygame.sprite.Sprite):
    number = random.randint(1, 3)

    def __init__(self, scroll_speed, x, y):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(assets_path, 'background', f'background_{Background.number}.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scroll_speed = scroll_speed

    def update(self):
        self.rect.y += self.scroll_speed
        win_height = pygame.display.get_surface().get_height()

        if self.rect.y >= win_height:
            self.rect.y = -(self.image.get_height() + self.image.get_height() - win_height)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity):
        super().__init__()
        self.list_image = []

        for i in range(1, 5):
            image = pygame.transform.scale2x(
                pygame.image.load(os.path.join(assets_path, 'player', f'player_{i}.png'))).convert()
            self.list_image.append(image)

        self.image_index = 0
        self.rect = self.list_image[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.velocity = velocity

    def handle_key(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity

        if keys[pygame.K_SPACE]:
            # ToDo make the interval of the shooting 0.5 or depends on the bullet
            pass

    def draw(self, screen):
        screen.blit(self.list_image[self.image_index])
