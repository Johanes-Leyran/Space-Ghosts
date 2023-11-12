import pygame
from space_ghost.entity import Background
pygame.init()

screen = pygame.display.set_mode((650, 750))
clock = pygame.time.Clock()

group = pygame.sprite.Group()
background_1 = Background(1, 1)
background_2 = Background(1, 2)

background_1.rect.y = -(background_1.image.get_height() - screen.get_height())
background_2.rect.y = -(background_2.image.get_height() * 2 - screen.get_height())

group.add(background_1, background_2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    clock.tick(40)
    group.update()
    group.draw(screen)
    pygame.display.flip()
