"""Class for food object"""
import random

import pygame


class Apple:
    """Generating the apples and handle them"""

    def __init__(self, snake_game):
        """Initialize the apple setting and the starting pos"""
        # Settings and screen
        self.settings = snake_game.settings
        self.window = snake_game.window

        # Image
        self.image = pygame.image.load(r'utils\Images\apple.png')
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.element_size, self.settings.element_size)
        )
        self.rect = self.image.get_rect()

        # Starting position
        self.pos_x_idx = 0
        self.pos_y_idx = 0
        self.new_pos(snake_game.snake.body, True)

        # Eating Flag
        self.eated = False

    def draw_apple(self):
        """Draw the apple to the screen"""
        self.rect.x = self.pos_x_idx * self.settings.case_width + 2
        self.rect.y = self.pos_y_idx * self.settings.case_width + 2

        self.window.blit(self.image, self.rect)

    def new_pos(self, body, start=False):
        """Generate a new position for the apple if this new position
        is not already occupied by the snake.

        Arguments:
            body {list} -- the list of the snake's body position
        """
        accepted_pos = [[idx_x, idx_y] \
            for idx_x in range(1, self.settings.nb_rows_x -1) \
            for idx_y in range(1, self.settings.nb_rows_y - 3)]

        for element in body:
            accepted_pos.remove(element)

        if start:
            accepted_pos.remove(
                [self.settings.nb_rows_x // 2, self.settings.nb_rows_y // 2])
        else:
            accepted_pos.remove([self.pos_x_idx, self.pos_y_idx])

        self.pos_x_idx, self.pos_y_idx = random.choice(accepted_pos)
