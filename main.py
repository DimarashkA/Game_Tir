import pygame
import random

pygame.init()

SCREEN_WIDHT = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/тир.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_widht = 80
target_height = 80

target_x = random.randint(0,SCREEN_HEIGHT - target_height)
target_y = random.randint(0,SCREEN_WIDHT - target_widht)

color = random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)

running = True

while running:
    pass

pygame.quit()



