import pygame
import sys


def terminate():
    pygame.quit()
    sys.exit()


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
rect = pygame.Rect(400, 400, 30, 30)
speed = 10
FPS = 120
jump = False
jumpCount = 0
jumpMax = 15

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                jumpCount = jumpMax

    pressed_keys = pygame.key.get_pressed()
    rect.centerx = (rect.centerx + (pressed_keys[pygame.K_d] -
                                      pressed_keys[pygame.K_a]) * speed) % 800
    if jump:
        rect.y -= jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False

    screen.fill((0, 0, 255))
    pygame.draw.rect(screen, (64, 64, 64), (0, 600, 1000, 800))
    pygame.draw.circle(screen, (255, 0, 0), rect.center, 15)
    pygame.display.flip()