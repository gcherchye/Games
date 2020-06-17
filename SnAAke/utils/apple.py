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
        self._get_starting_pos()

        # Eating Flag
        self.eated = False

    def _get_starting_pos(self):
        """Get a random starting position but not the snake's one"""
        accepted = list(range(0, self.settings.nb_rows))
        accepted.remove(self.settings.nb_rows // 2)

        self.pos_x_idx = random.choice(accepted)
        self.pos_y_idx = random.choice(accepted)

    def draw_apple(self):
        """Draw the apple to the screen"""
        self.rect.x = self.pos_x_idx * self.settings.case_width + 2
        self.rect.y = self.pos_y_idx * self.settings.case_width + 2

        self.screen.blit(self.image, self.rect)


    def is_eaten(self, head):
        """Check if the head of the snake collide with the apple
        i.e.: the apple is eaten by the snake
        """
        return self.rect.colliderect(head)

    def new_pos(self, body):
        """Generate a new position for the apple if this new position
        is not already occupied by the snake.

        Arguments:
            body {list} -- the list of the snake's body position
        """
        accepted_pos = [[idx_x, idx_y] \
            for idx_x in range(self.settings.nb_rows) \
            for idx_y in range(self.settings.nb_rows)]

        for element in body:
            accepted_pos.remove(element)

        accepted_pos.remove([self.pos_x_idx, self.pos_y_idx])

        self.pos_x_idx, self.pos_y_idx = random.choice(accepted_pos)
