import pygame
import os

assets_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
background_path = os.path.join(assets_path, 'background')
player_path = os.path.join(assets_path, 'player')


class Background(pygame.sprite.Sprite):
    def __init__(self, scroll_speed, index):
        super().__init__()
        self.image = pygame.image.load(os.path.join(background_path, f'background_{index}.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.scroll_speed = scroll_speed

    def update(self):
        window_height = pygame.display.get_surface().get_height()

        if self.rect.y >= window_height:
            self.rect.y = -((self.image.get_height() * 2) - window_height)

        self.rect.y += self.scroll_speed


class Player(pygame.sprite.Sprite):
    def __init__(self, initial_x, initial_y):
        super().__init__()

        self.ship_image_list = [pygame.transform.scale2x(
            pygame.image.load(os.path.join(player_path, f'player_{i}.png'))
        ).convert_alpha() for i in range(1, 5)]
        self.image_index = 0

        self.engine_image = pygame.transform.scale2x(
            pygame.image.load(os.path.join(player_path, 'engine.png'))).convert_alpha()
        self.engine_effects = pygame.transform.scale2x(
            pygame.image.load(os.path.join(player_path, 'engine_effects.png'))).convert_alpha()
        self.engine_effects_index = 0

        self.rect = self.ship_image_list[0].get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.health = 100.0
        self.velocity = 10

        self.last_engine_effect_time = pygame.time.get_ticks()
        self.last_bullet_fire = pygame.time.get_ticks()
        self.bullet_fire_available = True

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
            if self.bullet_fire_available:
                print('fire')
                self.last_bullet_fire = pygame.time.get_ticks()
                self.bullet_fire_available = False

    def update(self):
        if self.health / 100 <= 0.3:
            self.image_index = 3
        elif self.health / 100 <= 0.6:
            self.image_index = 2
        elif self.health / 100 <= 0.9:
            self.image_index = 1

        current_time = pygame.time.get_ticks()
        if current_time - self.last_engine_effect_time >= 150:
            self.engine_effects_index += 1
            self.last_engine_effect_time = current_time

        if not self.bullet_fire_available:
            if current_time - self.last_bullet_fire >= 500:
                self.bullet_fire_available = True

        if self.engine_effects_index > 4:
            self.engine_effects_index = 0

    def draw(self, screen):
        screen.blit(self.engine_image, (self.rect.x, self.rect.y + 5))
        screen.blit(self.engine_effects, (self.rect.x, self.rect.y + 5), (0 + (self.engine_effects_index * 96), 0, 96, 96))
        screen.blit(self.ship_image_list[self.image_index], (self.rect.x, self.rect.y))
