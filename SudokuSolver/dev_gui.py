"""dev file for the GUI"""
from __future__ import absolute_import

import pygame

from utils.settings import Settings

class Sudoku:
    """Sudoku class"""

    def __init__(self):
        """initialisation of the game and ressources"""
        # Game settings
        self.settings = Settings()

        # Game window
        self.window = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height)
        )
        pygame.display.set_caption('Sudoku')

        # Window field
        self.screen = pygame.Rect(
            self.settings.game_left,
            self.settings.game_top,
            self.settings.game_width,
            self.settings.game_height
        )

if __name__ == '__main__':
    sudoku = Sudoku()
