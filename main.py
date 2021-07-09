import logging
import sys

import pygame

from actors.bars import Bars
from actors.player import Player
from vars import BAR_HORIZONTAL_GAP, WINDOW_SCREEN, BAR_WIDTH, BAR_VERTICAL_GAP


def show_score(choice, color, font, size, score, window):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (720 / 10, 15)
    else:
        score_rect.midtop = (720 / 2, 480 / 1.25)
    window.blit(score_surface, score_rect)


def initialize_bars():
    bars = [Bars()]
    for bar in bars:
        if bar.x + BAR_HORIZONTAL_GAP < WINDOW_SCREEN[0]:
            bars.append(Bars(bar.x + BAR_HORIZONTAL_GAP))
            bar.created_next = True
    return bars


def run():
    pygame.init()
    window = pygame.display.set_mode(WINDOW_SCREEN)
    player = Player()
    bars = initialize_bars()
    font = pygame.font.SysFont('consolas', 32)
    score = 0

    while True:
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        window = player.move(window)
        prev_dist = 0
        for bar in bars:
            if bar.x + BAR_WIDTH < 0:
                score += 2
                bars.remove(bar)

            # Create new bars when far fro the right
            if bar.x + BAR_HORIZONTAL_GAP < WINDOW_SCREEN[0] and not bar.created_next:
                bars.append(Bars(bar.x + BAR_HORIZONTAL_GAP))
                bar.created_next = True

            if bar.x + BAR_WIDTH // 2 <= player.x and not bar.passed_player:
                logging.error(f'distance_surface: {player.x - bar.x}')
                pygame.draw.circle(window, (200, 0, 0), (bar.x + BAR_WIDTH / 2,
                                                         bar.lower_y - BAR_VERTICAL_GAP / 2), 10)
                logging.warning(f'My index: {bars.index(bar)}', )
                bar.passed_player = True
            k = 0
            if not bars[0].passed_player:
                first_bar = bars[k]
            else:
                k += 1
                print('changed bars')
                first_bar = bars[k]
            if first_bar.passed_player:
                logging.error('Invalid first bar')
            print(f'distance_surface: {first_bar.x - player.x}')
            distance = first_bar.x - player.x
            if distance <= 0:
                k += 1
                first_bar = bars[k]
            distance = first_bar.x - player.x

            distance_surface = font.render(f'distance: {distance}', True, (255, 255, 255), (0, 0, 0))
            rect = distance_surface.get_rect()
            rect.y = 80
            rect.x = 10
            window.blit(distance_surface, rect)
            prev_dist = distance
            window = bar.move(window)
            # player.collide(bar.obj_lower, bar.obj_upper, window)
        score_ = font.render(f'Score: {score}', True, (255, 255, 255), (0, 0, 0))
        score_rect = score_.get_rect()
        score_rect.y = 50
        score_rect.x = 10
        window.blit(score_, score_rect)

        pygame.display.update()
        pygame.time.Clock().tick(30)


if __name__ == '__main__':
    run()
