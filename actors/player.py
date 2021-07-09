import sys

import pygame

from vars import PLAYER_POS, WINDOW_SCREEN, game_over


class Player(object):
    def __init__(self):
        self.x = PLAYER_POS[0]
        self.y = PLAYER_POS[1]
        self.speed = 0

    def draw(self, surface: pygame.surface):
        self.obj = pygame.draw.circle(surface, (200, 128, 90), (self.x, self.y), 15)
        return surface

    def move(self, surface):
        speed = self.speed + 0.08 * 30
        # speed = 1
        self.y += self.speed
        self.speed = speed
        if self.speed > 15:
            self.speed = 20
        surface = self.draw(surface)
        return surface

    def collide(self, rect1, rect2, surface) -> None:
        if self.y + self.obj.height >= WINDOW_SCREEN[1] or self.y <= 0:
            self.y = WINDOW_SCREEN[1] - self.obj.width /2
            self.speed = 0
            game_over(surface)
            # sys.exit(0)
        if self.obj.colliderect(rect1) or self.obj.colliderect(rect2):
            game_over(surface)
            # pygame.quit()
            # sys.exit()

    def jump(self) -> None:
        # speed = self.speed - 1.5 * 30
        speed = -10
        self.y += speed
        self.speed = speed
