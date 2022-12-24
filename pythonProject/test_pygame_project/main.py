import pygame
import sys
import os


def terminate():
    pygame.quit()
    sys.exit()


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
rect_hero = pygame.Rect(400, 400, 30, 30)
speed = 10
FPS = 120
jump = False
jumpCount = 0
jumpMax = 15


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f'Файл с рисунком "{fullname}" не найден!')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is None:
        image.convert_alpha()
    else:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class MainHero(pygame.sprite.Sprite):
    image = load_image("mar.png")

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = MainHero.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y


all_sprites = pygame.sprite.Group()
main_hero = MainHero(300, 500)
all_sprites.add(main_hero)
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
    rect_hero.centerx = (rect_hero.centerx + (pressed_keys[pygame.K_d] -
                                    pressed_keys[pygame.K_a]) * speed) % 800
    if jump:
        rect_hero.y -= jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False
    all_sprites.update(rect_hero.x, rect_hero.y)
    screen.fill((0, 0, 255))
    pygame.draw.rect(screen, pygame.Color('brown'), (0, 435, 800, 600))
    '''pygame.draw.rect(screen, (64, 64, 64), (0, 600, 1000, 800))
    pygame.draw.circle(screen, (255, 0, 0), rect.center, 15)'''
    all_sprites.draw(screen)
    pygame.display.flip()
