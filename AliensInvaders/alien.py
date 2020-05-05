"""The class to manage the aliens."""
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attr
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x_pos = float(self.rect.x)

    def check_edge(self):
        """Return True if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self, *args):
        """Move the aliens to the right or left"""
        self.x_pos += (self.settings.alien_speed *
                      self.settings.fleet_direction)
        self.rect.x = self.x_pos
