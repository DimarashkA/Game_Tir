import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/тир.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)

font = pygame.font.Font(None, 36)

hits = 0
misses = 0
start_time = time.time()
game_duration = 30  # Game duration in seconds

running = True

while running:
    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_duration - elapsed_time)

    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                misses += 1

    screen.blit(target_img, (target_x, target_y))

    score_text = font.render(f'Попадания: {hits} Промахи: {misses}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    timer_text = font.render(f'Время: {int(remaining_time)}', True, (255, 255, 255))
    screen.blit(timer_text, (10, 50))

    pygame.display.update()

    if elapsed_time >= game_duration:
        running = False

pygame.quit()

print(f'Игра закончена! Всего попаданий: {hits}, Всего промахов: {misses}')




