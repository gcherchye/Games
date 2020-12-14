"""The Settings used in the game."""
from __future__ import absolute_import

import json

CONFIG_PATH = 'config.json'

# TODO: the speedup scale can be transform into a level selection where 1.05 is easy and 1.2 is hard

class Settings:
    """1-2 1-2 this is a test"""

    def __init__(self) -> None:
        super().__init__()

        with open(CONFIG_PATH, 'r') as config_file:
            self.config = json.load(config_file)

        print(type(self.config.get('static')))
        print(self.config.get('static'))

        for key, value in self.config.get('static').items():
            setattr(self, key, value)

        self.init_dynamic()

    def init_dynamic(self) -> None:
        """Initialize the attributes that will change through the game"""
        for key, value in self.config.get('dynamic').items():
            setattr(self, key, value)

    def increase_stats(self):
        """Increase the speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.scoring_scale)
