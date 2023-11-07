from entity import Background, Player
import time
import pygame
pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 750
FPS = 30

scroll_speed = 2
background_color = (0, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('Space Ghost')

clock = pygame.time.Clock()
prev_time = time.time()

background_1 = Background(scroll_speed, 0, 0)
background_2 = Background(scroll_speed, 0, 0)

# background_1.rect.y = -(background_1.image.get_height() - WINDOW_HEIGHT)
background_1.rect.y = -(background_1.image.get_height() - WINDOW_HEIGHT)
background_2.rect.y = -(background_2.image.get_height() + background_1.image.get_height() - WINDOW_HEIGHT)

background_group = pygame.sprite.Group(background_1, background_2)

player = Player(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, 10)

# makes the cursor disappear when playing the game
# pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))


def handle_background():
    background_group.update()
    background_group.draw(screen)


running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ToDo organize handling the key pressed
    player.handle_key()

    screen.fill((100, 100, 100))
    handle_background()

    clock.tick(FPS)
    pygame.display.flip()
