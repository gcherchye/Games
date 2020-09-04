"""Define the scoreboard"""
import pygame.font


class Scoreboard:
    """Class to report scoring information"""

    def __init__(self, snake_game):
        """Initialize scorekeeping attributes"""
        self.snake_game = snake_game

        self.font_score = pygame.font.SysFont(None, 25)
        self.font_game_over = pygame.font.SysFont(None, 55)

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
        self.score_image = self.font_score.render(
            score_str,
            True,
            self.snake_game.settings.score_color,
        )
        # Set the score at the bottom left corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = self.snake_game.settings.window_height - 50
        self.score_rect.left = 25

    def show_score(self):
        """Show the score on the screen"""
        self.snake_game.window.blit(self.score_image, self.score_rect)

    def prep_game_over(self):
        """Prep the game over image"""
        game_over = f'Game Over !\nYou win {self.score} points !'

        # Loop for multilines message
        for index, line in enumerate(game_over.splitlines()):
            self.line_image = self.font_game_over.render(
                line,
                True,
                self.snake_game.settings.score_color
            )
            self.line_rect = self.line_image.get_rect()
            game_over_offset = index * self.line_rect.height
            self.line_rect.centery = (
                self.snake_game.screen.centery
                - self.snake_game.screen.height / 4) + game_over_offset
            self.line_rect.centerx = self.snake_game.screen.centerx
            self.snake_game.window.blit(self.line_image, self.line_rect)
