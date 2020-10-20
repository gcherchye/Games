"""Setting class for the sudoku"""
from __future__ import absolute_import


class Settings():
    """Settings for the sudoku game"""

    def init(self):
        """initialize settings for the sudoku game"""
        self.window_width = 42
        self.window_height = 42

        self.game_width = 525
        self.game_height = 525
        self.game_left = 25
        self.game_top = 25
        self.game_border_color = (200, 200, 200)