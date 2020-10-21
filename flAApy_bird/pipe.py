"""Some pipes to kill the dumbest flap"""
from __future__ import absolute_import

import pygame

from settings import Settings

class Pipe:
    """The Mario's friends"""
    def __init__(self, x) -> None:
        self.settings = Settings()

        self.x = x
        self.height = 0
        self.gap = 100
        self.PIPE_TOP = pygame.transform.flip(self.settings.pipe_img, False, True)
        self.PIPE_BOTTOM = self.settings.pipe_img
