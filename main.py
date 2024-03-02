import pygame
import sys
import os
import random


pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
FPS = 60
W = 1200
H = 800
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

from load import *

def game_lvl():
    sc.fill("gray")
    food_group.update()
    food_group.draw(sc)
    pygame.display.update()

class Food(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, W - 100)
        self.rect.y = random.randint(100, H - 100)

def restart():
    global player_group, food_group, enemy_1_group, enemy_2_group
    player_group = pygame.sprite.Group()
    food_group = pygame.sprite.Group()
    enemy_1_group = pygame.sprite.Group()
    enemy_2_group = pygame.sprite.Group()
restart()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if len(food_group) < 20:
        food = Food(food_image)
        food_group.add(food)
    game_lvl()
    clock.tick(FPS)
