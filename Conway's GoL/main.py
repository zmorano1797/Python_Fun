import time
import pygame
import numpy as np
import tkinter as tk
from tkinter import simpledialog

COLO_BG = (10,10,10)
COLOR_GRID = (40,40,40)
COLOR_DIE_NEXT = (170,170,170)
COLOR_ALIVE_NEXT = (255,255,255)

size1grid = simpledialog.askinteger("Length:", "How many Pixels Long?")
size2grid = simpledialog.askinteger("Width:", "How many Pixels Wide?")

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0],cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLO_BG if cells[row,col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
    
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((size1grid, size2grid))

    size1 = int(size2grid/10)
    size2 = int(size1grid/10)

    cells = np.zeros((size1, size2))
    screen.fill((COLOR_GRID))
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == '__main__':
    main()