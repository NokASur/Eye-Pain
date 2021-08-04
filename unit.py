import random
import pygame


W = 1000
H = 500


class Unit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.w = random.randint(2, 3) * 10
        self.h = random.randint(2, 3) * 10
        self.image = pygame.Surface((self.w, self.h))
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.image.fill(self.color)
        self.speed = 10
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(0, W - self.w) + self.w // 2, random.randint(0, H - self.h) + self.h // 2]

    def update(self):
        direction = random.randint(0, 3)
        if direction == 1:
            self.rect.y -= self.speed
        elif direction == 2:
            self.rect.x += self.speed
        elif direction == 3:
            self.rect.y += self.speed
        else:
            self.rect.x -= self.speed
        if 0 > self.rect.x:
            self.rect.x = 0
        if self.rect.x > W:
            self.rect.x = W
        if self.rect.y > H:
            self.rect.y = H
        if self.rect.y < 0:
            self.rect.y = 0

