"""Define the scoreboard"""
import pygame.font


class Scoreboard:
    """Class to report scoring information"""

    def __init__(self, snake_game):
        """Initialize scorekeeping attributes"""
        self.snake_game = snake_game
        self.window = self.snake_game.window
        self.screen_rect = self.snake_game.screen
        self.settings = self.snake_game.settings

        self.color = self.settings.score_color
        self.font = pygame.font.SysFont(None, 25)

        self.reset_score()
        self.prep_score()

        self.prep_game_over()

    def reset_score(self):
        """Reinitialize the score"""
        self.score = 0
        self.prep_score()

    def prep_score(self):
        """Turn score into a rendered image"""
        # Create the score image
        score_str = f'Score : {self.score:,}'
        self.score_image = self.font.render(
            score_str,
            True,
            self.color,
        )
        # Set the score at the top-right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = self.settings.window_height - 50
        self.score_rect.left = 25

    def show_score(self):
        """Show the score on the screen"""
        self.window.blit(self.score_image, self.score_rect)

    def prep_game_over(self):
        """Prep the game over image"""
        game_over = f'Game Over !\nYou win {self.score} points !'

        for index, line in enumerate(game_over.splitlines()):
            self.line_image = self.font.render(
                line,
                True,
                self.color
            )
            self.line_rect = self.line_image.get_rect()
            game_over_offset = index * self.line_rect.height
            self.line_rect.centery = (
                self.screen_rect.centery
                - self.screen_rect.height / 4) + game_over_offset
            self.line_rect.centerx = self.screen_rect.centerx
            self.window.blit(self.line_image, self.line_rect)
