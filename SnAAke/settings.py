"""Settings class for the whole game"""


class Settings:
    """Store the settings for SnAAke game"""

    def __init__(self):
        """Initialize static settings for the game"""
        # Screen settings
        self.screen_width = 525
        self.screen_height = 525
        self.nb_rows = 21
        self.case_width = self.screen_width // self.nb_rows
        self.back_color = (25, 25, 25)
        self.line_color = (150, 150, 150)

        # Snake settings
        self.snake_color = (0, 204, 0)
        self.snake_speed = 1

        # Apple settings
        self.apple_color = (250, 0, 0)
