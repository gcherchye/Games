"""Settings class for the whole game"""


class Settings:
    """Store the settings for SnAAke game"""

    def __init__(self):
        """Initialize static settings for the game"""
        # Screen settings
        self.fps = 30

        self.window_width = 575
        self.window_height = 625

        self.game_width = 525
        self.game_height = 525
        self.game_left = 25
        self.game_top = 25
        self.game_border_color = (200, 200, 200)

        self.nb_rows_x = 23
        self.nb_rows_y = 25
    
        self.case_width = self.window_width // self.nb_rows_x

        self.back_color = (25, 25, 25)

        # All element settings
        self.element_size = self.case_width - 2

        # Snake settings
        self.snake_color = (0, 204, 0)
        self.snake_speed = 1

        # Scoring settings
        self.score_color = (200, 200, 200)
        self.score_increment = 5
