"""The almighty SnAAke game"""
from __future__ import absolute_import

import pygame

from utils.apple import Apple
from utils.button import PlayButton, ExitButton, RestartButton
from utils.scoreboard import Scoreboard
from utils.settings import Settings
from utils.snake import Snake


class SnakeGame:
    """Overall Class to manage game and behavior"""

    def __init__(self):
        """Initialize the game and create game's ressources"""
        # Game settings
        self.settings = Settings()

        # Pygame intiliazing
        pygame.init()

        # Game Window
        self.window = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height)
        )
        pygame.display.set_caption('SnAAke')

        # Window field
        self.screen = pygame.Rect(
            self.settings.game_left,
            self.settings.game_top,
            self.settings.game_width,
            self.settings.game_height
        )

        # Setting the clock
        self.clock = pygame.time.Clock()

        # Game modules
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.scoreboard = Scoreboard(self)

        # Game button
        self.play_button = PlayButton(self, 'Play')
        self.exit_button = ExitButton(self, 'Exit')
        self.restart_button = RestartButton(self, 'Restart')

        # Game flags
        self.game_over = False
        self.pause = False
        self.play = True
        self.run = False

    def run_game(self):
        """Main game's loop"""
        while self.play:
            # Tick the clock
            delta_t = self.clock.tick(self.settings.fps)

            # Check user input
            self._check_events()

            if self.run and not self.pause:
                self.snake.move(delta_t)
                self._check_eating()

            # Update the screen
            self._update_screen()

    def _check_events(self):
        """Response to keypresses and mouse events"""
        for event in pygame.event.get():
            # Exit button on the window
            if event.type == pygame.QUIT:
                self.play = False

            # Mouse button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.game_over:
                    self._check_play_button(mouse_pos)
                elif self.game_over:
                    self._check_restart_or_exit(mouse_pos)

            # Keyboard
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_play_button(self, mouse_pos):
        """Start the game if the 'Play' button is pressed

        Args:
            mouse_pos (tuple): the coordinate of the mouse when the click occurs
        """
        button_click = self.play_button.rect.collidepoint(mouse_pos)
        if button_click and not self.run:
            self._start_game()

    def _start_game(self):
        """Handle starting event"""
        # Activate the game
        self.run = True

        # Deactivate the mouse
        pygame.mouse.set_visible(False)

        # Prep the score
        self.scoreboard.prep_score()

    def _check_restart_or_exit(self, mouse_pos):
        """Check if the restart or the exit button is clicked

        Args:
            mouse_pos (tuple): the coordinate of the mouse when the click occurs
        """
        exit_clicked = self.exit_button.rect.collidepoint(mouse_pos)
        restart_clicked = self.restart_button.rect.collidepoint(mouse_pos)

        if exit_clicked:
            self.play = False
        if restart_clicked:
            self._restart_game()

    def _restart_game(self):
        """Handle restart events"""
        # Reset the score
        self.scoreboard.reset_score()

        # Reset the snake
        self.snake.reset_snake()

        # Reset the flags
        self.run = True

    def _check_keydown_events(self, event):
        """Check which keyboard's key is pressed and react to it

        Args:
            event (object): a pygame event for event.type == pygame.KEYDOWN
        """
        # Escape key - quiy
        if event.key == pygame.K_ESCAPE:
            self.play = False
        # Space bar/p - Pause
        elif event.key in (pygame.K_SPACE, pygame.K_p):
            if self.pause:
                self.pause = False
            else:
                self.pause = True
        # ZQSD/arrow - mouvement
        if not self.snake.move_recorded:
            if event.key in (pygame.K_UP, pygame.K_w):
                self.snake.change_direction('up')
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.snake.change_direction('down')
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                self.snake.change_direction('left')
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.snake.change_direction('right')

    def _check_eating(self):
        """Trigger the events if the snake eat the apple"""
        if self.apple.rect.colliderect(self.snake.head_rect) and not self.apple.eated:
            self.scoreboard.score += self.settings.score_increment
            self.scoreboard.prep_score()

            self.apple.new_pos(self.snake.body)
            self.apple.eated = True

            self.snake.add_unit()
            self.snake.speed *= self.settings.snake_speed_incr

        if self.snake.moved:
            self.apple.eated = False

    def _update_screen(self):
        """Update the images on the screen and flip to the new screen"""
        # Fill the screen with background color
        self.window.fill(self.settings.back_color)

        if self.run:
            # Draw the field
            pygame.draw.rect(
                self.window,
                self.settings.game_border_color,
                self.screen,
                1
            )

            # Draw the apple and the snake
            self.apple.draw_apple()
            self.snake.draw_snake()

            # Draw the score
            self.scoreboard.show_score()

        # Check self eating
        if self.snake.is_self_collision():
            self._game_over()

        # Draw the play button if needed
        if not self.run and not self.game_over:
            self.play_button.draw()

        # Update the screen
        pygame.display.flip()

    def _game_over(self):
        """Handle the game over"""
        # Exit the game loop
        self.run = False
        self.game_over = True

        # Reactivate the mouse
        pygame.mouse.set_visible(True)

        # Display 'Game Over' to the screen
        self.scoreboard.prep_game_over()
        self.exit_button.draw()
        self.restart_button.draw()


if __name__ == '__main__':
    snake = SnakeGame()
    snake.run_game()
