import pygame
import sys
import random

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 1200, 750
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")

# Colors
BACKGROUND_COLOR = (0, 0, 0)
BAR_BORDER_COLOR = (0, 0, 0)
BAR_START_COLOR = (20, 200, 135)  
BAR_END_COLOR = (72, 61, 139)    

# Bar settings
BAR_WIDTH = 10
GAP = 2
NUM_BARS = WIDTH // (BAR_WIDTH + GAP)
bars = [random.randint(50, 700) for _ in range(NUM_BARS)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr.copy()

# Map values to gradient colors
def map_color(value, start_color, end_color, start_value, end_value):
    progress = (value - start_value) / (end_value - start_value)
    r = int(start_color[0] + progress * (end_color[0] - start_color[0]))
    g = int(start_color[1] + progress * (end_color[1] - start_color[1]))
    b = int(start_color[2] + progress * (end_color[2] - start_color[2]))
    return r, g, b

# Main loop
clock = pygame.time.Clock()
running = True
sort_gen = bubble_sort(bars)
speed = 3  # Adjust the speed here (lower is faster)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    try:
        for _ in range(speed):
            new_bars = next(sort_gen)
        bars = new_bars
    except StopIteration:
        pass

    win.fill(BACKGROUND_COLOR)

    for i, bar in enumerate(bars):
        color = map_color(bar, BAR_START_COLOR, BAR_END_COLOR, 0, 700)
        pygame.draw.rect(win, color, (i * (BAR_WIDTH + GAP), HEIGHT - bar, BAR_WIDTH, bar))
        pygame.draw.rect(win, BAR_BORDER_COLOR, (i * (BAR_WIDTH + GAP), HEIGHT - bar, BAR_WIDTH, bar), 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
