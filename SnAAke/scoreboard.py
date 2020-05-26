"""Define the scoreboard"""
import pygame.font 


class Scoreboard:
    """Class to report scoring information"""

    def __init__(self, snake_game):
        """Initialize scorekeeping attributes"""
        self.snake_game = snake_game
        self.screen = self.snake_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = self.snake_game.settings

        self.color = self.settings.score_color
        self.font = pygame.font.SysFont(None, 48)

        self.reset_score()
        self.prep_score()

    def reset_score(self):
        """Reinitialize the score"""
        self.score = 0

    def prep_score(self):
        """Turn score into a rendered image"""
        # Create the score image
        score_str = '{:,}'.format(self.score)
        self.score_image = self.font.render(
            score_str,
            True,
            self.color,
        )
        # Draw the score at the top-right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right -20

    def show_score(self):
        """Show the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
