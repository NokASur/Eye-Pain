import random, pygame, time
from unit import *

fpsClock = pygame.time.Clock()
pygame.init()
FPS = 90
W = 1000
H = 500
rect_amount = random.randint(60, 65)
window_size = (W, H)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Color_trash")
inGame = True
all_sprites = pygame.sprite.Group()
for rect in range(rect_amount):
    new_rect = Unit()
    all_sprites.add(new_rect)

while inGame:
    fpsClock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
    all_sprites.update()
    screen.fill([0, 0, 0])
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
