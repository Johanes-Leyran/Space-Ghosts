from game import Background, Player
import pygame
pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 750
FPS = 30

scroll_speed = 2
background_color = (0, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('Space Raiders')

clock = pygame.time.Clock()
prev_time = pygame.time.get_ticks()

# ToDo change the list into pygame group
background_group = pygame.sprite.Group()
background_1 = Background(scroll_speed, 0, 0)
background_2 = Background(scroll_speed, 0, 0)

# background_1.rect.y = -(background_1.image.get_height() - WINDOW_HEIGHT)
background_1.rect.y = -(background_1.image.get_height() - WINDOW_HEIGHT)
background_2.rect.y = -(background_2.image.get_height() + background_1.image.get_height() - WINDOW_HEIGHT)

background_group.add(background_1, background_2)

running = True

player = Player(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)


def handle_background():
    background_group.update()
    background_group.draw(screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ToDo organize handling the key pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.position[0] -= 10
    if keys[pygame.K_RIGHT]:
        player.position[0] += 10
    if keys[pygame.K_UP]:
        player.position[1] -= 5
    if keys[pygame.K_DOWN]:
        player.position[1] += 5

    # Todo implement proper delta time
    current_time = pygame.time.get_ticks()
    delta_time = (current_time - prev_time) / 1000.0

    screen.fill((100, 100, 100))
    handle_background()
    player.draw(screen)

    clock.tick(FPS)
    pygame.display.flip()
