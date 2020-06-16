"""Settings class for the whole game"""


class Settings:
    """Store the settings for SnAAke game"""

    def __init__(self):
        """Initialize static settings for the game"""
        # Screen settings
        self.fps = 10
        self.screen_width = 525
        self.screen_height = 525
        self.nb_rows = 21
        self.case_width = self.screen_width // self.nb_rows
        self.back_color = (25, 25, 25)

        # All element settings
        self.element_size = self.case_width - 2

        # Snake settings
        self.snake_color = (0, 204, 0)
        self.snake_speed = 1

        # Scoring settings
        self.score_color = (200, 200, 200)
        self.score_increment = 5
