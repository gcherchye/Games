"""Class for food object"""
import random

import pygame


class Apple:
    """Generating the apples and handle them"""

    def __init__(self, snake_game):
        """Initialize the apple setting and the starting pos"""
        # Settings and screen
        self.settings = snake_game.settings
        self.screen = snake_game.screen

        # Starting position
        self._get_starting_pos()

        self.color = self.settings.apple_color
        self.size = self.settings.case_width - 4

        self.apple = pygame.Rect(
            self.pos_x_idx * self.settings.case_width + 2,
            self.pos_y_idx * self.settings.case_width + 2,
            self.size,
            self.size
        )

    def _get_starting_pos(self):
        """Get a random starting position but not the snake's one"""
        accepted = list(range(0, self.settings.nb_rows))
        accepted.remove(self.settings.nb_rows // 2)

        self.pos_x_idx = random.choice(accepted)
        self.pos_y_idx = random.choice(accepted)

    def draw_apple(self):
        """Draw the apple to the screen"""
        pygame.draw.rect(
            self.screen,
            self.color,
            self.apple
        )

    def is_eaten(self, head):
        """Check if the head of the snake collide with the apple
        i.e.: the apple is eaten by the snake
        """
        return self.apple.colliderect(head)

    def new_pos(self):
        """Generate a new position for the apple"""
        self.pos_x_idx = random.randint(0, self.settings.nb_rows - 1)
        self.pos_y_idx = random.randint(0, self.settings.nb_rows - 1)
