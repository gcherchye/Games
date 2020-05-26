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
        # Set the score at the top-right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right -20

    def show_score(self):
        """Show the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)

    def show_game_over(self):
        """Show the Game over screen and buttons"""
        self._prep_game_over_text()
        

    def _prep_game_over_text(self):
        """Prep the game over image"""
        game_over = f'Game Over !\nYour win {self.score} points !'

        for index, line in enumerate(game_over.splitlines()):
            line_image = self.font.render(
                line,
                True,
                self.color
            )
            line_rect = line_image.get_rect()
            game_over_offset = (0, index * line_rect.height)
            line_rect.center = tuple(map(sum, zip(self.screen_rect.center, game_over_offset)))

            self.screen.blit(line_image, line_rect)
