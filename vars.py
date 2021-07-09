import sys
import time

import pygame.font

WINDOW_SCREEN = 720, 480
PLAYER_POS = 720 / 2 - 200, 480 / 4
BAR_HEIGHT, BAR_WIDTH = 250, 50
BAR_HORIZONTAL_GAP = 150
BAR_VERTICAL_GAP = 150

def game_over(surface):
    font = pygame.font.SysFont('consolas', 50)
    disp = font.render('GAME OVER', True, (180, 190, 200), (0, 0, 0))
    disp_rect = disp.get_rect()
    disp_rect.centerx = WINDOW_SCREEN[0] // 2
    disp_rect.centery = WINDOW_SCREEN[1] // 2
    surface.fill((0, 0, 0))
    surface.blit(disp, disp_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit(1)

