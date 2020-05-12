"""The Settings used in the game."""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (98, 181, 229)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_drop_speed = 10

        # Leveling settings
        self.speedup_scale = 1.1  #TODO: 1.05 == easy, 1.1 == normal, 1.2 == hard

        # Scoring settings
        self.score_scale = 1.5

        # Dynamic settings
        self.initiate_dynamic_settings()

    def initiate_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0

        # Scoring
        self.alien_points = 50

        # Fleet direction : 1 = right, -1 = left
        self.fleet_direction = 1

    def increase_stats(self):
        """Increase the speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
