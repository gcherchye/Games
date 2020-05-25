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
            pygame.time.delay(50)
            self.clock.tick(20)

            self._check_events()

            self._update_screen()

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

    def _update_screen(self):
        """Update the images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.back_color)
        self._draw_grid()

        self.apple.draw_apple()
        self.snake.draw_snake()

        pygame.display.flip()

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

# def main():

#     s = snake((255, 0, 0), (10, 10))
