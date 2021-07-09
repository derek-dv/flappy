import random

import pygame

from vars import PLAYER_POS, BAR_WIDTH, BAR_HEIGHT, WINDOW_SCREEN, BAR_VERTICAL_GAP


class Bars(object):
    def __init__(self, x=PLAYER_POS[0] + 100):
        self.x = x
        self.upper_y = random.randint(-50,0)
        self.lower_y = self.upper_y + BAR_HEIGHT + BAR_VERTICAL_GAP
        self.created_next = False
        self.passed_player = False

    def draw(self, surface:pygame.surface):
        self.obj_upper = pygame.draw.rect(surface, (0,100,0), (self.x, self.upper_y, BAR_WIDTH, BAR_HEIGHT))
        self.obj_lower = pygame.draw.rect(surface, (0, 100, 0), (self.x, self.lower_y, BAR_WIDTH, BAR_HEIGHT))
        return surface

    def move(self, surface):
        self.x -= 2
        surface = self.draw(surface)
        return surface