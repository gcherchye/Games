"""The bullet class"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage the bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create the bullet at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the position as a decimal
        self.y_pos = float(self.rect.y)

    def update(self, *args):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y_pos -= self.settings.bullet_speed
        self.rect.y = self.y_pos

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
