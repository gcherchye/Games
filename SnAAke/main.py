"""The almighty SnAAke game"""
from __future__ import absolute_import

import pygame

from apple import Apple
from settings import Settings
from snake import Snake


class SnakeGame:
    """Overall Class to manage game and behavior"""

    def __init__(self):
        """Initialize the game and create game's ressources"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('SnAAke')

        self.apple = Apple(self)
        self.snake = Snake(self)

        self.run = True

    def run_game(self):
        """Main game's loop"""
        while self.run:
            self.clock.tick(10)

            # Check user input
            self._check_events()

            # Move the snake and check what the the new pos implies
            self.snake.move()
            if self.snake.is_collision():
                self.run = False
            self._check_eating()

            self._update_screen()

            if self.snake.is_collision():
                self.run = False

        pygame.quit()

    def _check_events(self):
        """Response to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Responses to keys pressed"""
        if event.key == pygame.K_ESCAPE:
            self.run = False
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.snake.change_direction('up')
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.snake.change_direction('down')
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.snake.change_direction('left')
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            self.snake.change_direction('right')

    def _update_screen(self):
        """Update the images on the screen and flip to the new screen"""
        # Fill the screen with background color and draw the grid
        self.screen.fill(self.settings.back_color)
        self._draw_grid()        

        # Draw the apple and the snake
        self.apple.draw_apple()
        self.snake.draw_snake()

        # Update the screen
        pygame.display.flip()

    def _check_eating(self):
        if self.apple.is_eaten(self.snake.head):
            # TODO: Update score
            # TODO: Prep score
            # TODO: check highscore

            self.apple.new_pos(self.snake.body)
            self.snake.add_unit()

    def _draw_grid(self):
        """Draw the grid on the screen"""
        line_mark_x = 0
        line_mark_y = 0

        for _ in range(self.settings.nb_rows):
            line_mark_x += self.settings.case_width
            line_mark_y += self.settings.case_width

            # Draw the horizontal lines
            pygame.draw.line(
                self.screen,
                self.settings.line_color,
                (line_mark_x, 0),  # Begin point of the line
                (line_mark_x, self.settings.screen_width)  # End point
            )
            # Draw the vertical lines
            pygame.draw.line(
                self.screen,
                self.settings.line_color,
                (0, line_mark_y),  # Begin point of the line
                (self.settings.screen_width, line_mark_y)  # End point
            )


if __name__ == '__main__':
    snake = SnakeGame()
    snake.run_game()
