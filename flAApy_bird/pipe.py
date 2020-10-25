"""Some pipes to kill the dumbest flap"""
from __future__ import absolute_import

import random

import pygame

from settings import Settings


class Pipe:
    """The Mario's friends"""
    def __init__(self, x) -> None:
        self.settings = Settings()

        self.x_coord = x
        self.height = 0
        self.pipe_top = pygame.transform.flip(self.settings.pipe_img, False, True)
        self.pipe_bottom = self.settings.pipe_img

        self.passed = False
        self.set_height()

    def set_height(self):
        """Set randomly the height of the border of the pipes"""
        self.height = random.randrange(50, 450)
        self.top = self.height - self.pipe_top.get_height()
        self.bottom = self.height + self.settings.gap

    def move(self):
        """Move the position of the pipe"""
        self.x_coord -= self.settings.pipe_vel

    def draw(self, win: pygame.Surface) -> None:
        """Draw the bottom & top pipes to the screen

        Args:
            win (pygame.Surface): The pygame screen for the game
        """
        win.blit(self.pipe_top, (self.x_coord, self.top))
        win.blit(self.pipe_bottom, (self.x_coord, self.bottom))

    def collide(self, bird: object) -> bool:
        """Check if a bird collide with the pipes using the mask of
        the bird and the mask of the pipes.

        Args:
            bird (object): the bird object

        Returns:
            bool: True if collide - False if otherwise
        """
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.pipe_top)
        bottom_mask = pygame.mask.from_surface(self.pipe_bottom)

        top_offset = (self.x_coord - bird.x_coord, self.top - round(bird.y_coord))
        bottom_offset = (self.x_coord - bird.x_coord, self.bottom - round(bird.y_coord))

        bottom_col = bird_mask.overlap(bottom_mask, bottom_offset)
        top_col = bird_mask.overlap(top_mask, top_offset)

        if bottom_col or top_col:
            return True

        return False
