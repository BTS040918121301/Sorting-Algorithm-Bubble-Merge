import pygame
import sys
import random

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 1200, 750
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Merge Sort Visualization")

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

# Merge Sort
def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        yield from merge_sort(arr, l, mid)
        yield from merge_sort(arr, mid + 1, r)
        yield from merge(arr, l, mid, mid + 1, r)

def merge(arr, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    while i <= y1 and j <= y2:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= y1:
        temp.append(arr[i])
        i += 1
    while j <= y2:
        temp.append(arr[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        arr[i] = temp[j]
        j += 1
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
merge_sort_generator = merge_sort(bars, 0, len(bars) - 1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    try:
        new_bars = next(merge_sort_generator)
    except StopIteration:
        pass

    win.fill(BACKGROUND_COLOR)

    for i, bar in enumerate(new_bars):
        color = map_color(bar, BAR_START_COLOR, BAR_END_COLOR, 0, 700)
        pygame.draw.rect(win, color, (i * (BAR_WIDTH + GAP), HEIGHT - bar, BAR_WIDTH, bar))
        pygame.draw.rect(win, BAR_BORDER_COLOR, (i * (BAR_WIDTH + GAP), HEIGHT - bar, BAR_WIDTH, bar), 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
