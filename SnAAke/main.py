"""The almighty SnAAke game"""
from __future__ import absolute_import

from time import sleep

import pygame

from apple import Apple
from scoreboard import Scoreboard
from settings import Settings
from snake import Snake


class SnakeGame:
    """Overall Class to manage game and behavior"""

    def __init__(self):
        """Initialize the game and create game's ressources"""
        # Game settings
        self.settings = Settings()

        # Pygame intiliazing
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('SnAAke')
        self.clock = pygame.time.Clock()

        # Game modules
        self.apple = Apple(self)
        self.scoreboard = Scoreboard(self)
        self.snake = Snake(self)

        # Game parameters
        self.play = True
        self.run = True

    def run_game(self):
        """Main game's loop"""
        while self.play:
            # Tick the clock
            self.clock.tick(10)

            # Check user input
            self._check_events()

            if self.run:
                # Move the snake and check what the the new pos implies
                self.snake.move()
                self._check_eating()

                # Update the screen
                self._update_screen()

            # Tick the clock
            if self.snake.is_collision():
                self._game_over()

            #pygame.display.update()

    def _check_events(self):
        """Response to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Responses to keys pressed"""
        if event.key == pygame.K_ESCAPE:
            self.play = False
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.snake.change_direction('up')
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.snake.change_direction('down')
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.snake.change_direction('left')
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            self.snake.change_direction('right')

    def _check_eating(self):
        if self.apple.is_eaten(self.snake.head):
            self.scoreboard.score += self.settings.score_increment
            self.scoreboard.prep_score()

            self.apple.new_pos(self.snake.body)
            self.snake.add_unit()

    def _update_screen(self):
        """Update the images on the screen and flip to the new screen"""
        # Fill the screen with background color and draw the grid
        self.screen.fill(self.settings.back_color)

        # Draw the apple and the snake
        self.apple.draw_apple()
        self.snake.draw_snake()

        # Draw the score
        self.scoreboard.show_score()

        # Update the screen
        pygame.display.flip()

    def _game_over(self):
        """Handle the game over"""
        # Exit the game loop
        self.run = False

        # Display game Over to the screen
        self.scoreboard.show_game_over()
        pygame.display.flip()


if __name__ == '__main__':
    snake = SnakeGame()
    snake.run_game()
