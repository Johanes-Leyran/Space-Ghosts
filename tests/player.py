import pygame
from space_ghost.entity import Player
pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

player = Player(10, 10)
player_group = pygame.sprite.Group()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    player.draw(screen)
    player.update()
    player.handle_key()

    clock.tick(40)
    pygame.display.flip()
