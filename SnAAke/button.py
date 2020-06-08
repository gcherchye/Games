"""Classes to handle buttons"""
import pygame


class PlayButton:
    """The play button and the start screen"""

    def __init__(self, snake_game, msg):
        self.screen = snake_game.screen
        self.screen_rect = self.screen.get_rect()

        # Buttons settings
        self.width, self.height = 150, 50
        self.button_color = snake_game.settings.back_color
        self.text_color = snake_game.settings.snake_color
        self.font = pygame.font.SysFont(None, 48)

        # Center button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prep the button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Prep the message of the button in a rendered image"""
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_color,
            self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_play(self):
        """Draw the button on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        pygame.draw.rect(
            self.screen,
            self.text_color,
            self.rect,
            1  # width
        )


class ExitButton:
    """The Exit buttons and its parameters"""

    def __init__(self, snake_game, msg):
        self.screen = snake_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 150, 50
        self.button_color = snake_game.settings.back_color
        self.text_color = snake_game.settings.snake_color
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.width / 4
        self.rect.centery = 3 * self.screen_rect.height / 4

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Prep the message of the button in a rendered image"""
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_color,
            self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_exit(self):
        """Draw the button on the screen"""
        self.screen.blit(self.msg_image, self.msg_image_rect)
        pygame.draw.rect(
            self.screen,
            self.text_color,
            self.rect,
            1  # width
        )


class RestartButton:
    """The Exit buttons and its parameters"""

    def __init__(self, snake_game, msg):
        self.screen = snake_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 150, 50
        self.button_color = snake_game.settings.back_color
        self.text_color = snake_game.settings.snake_color
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = 3 * self.screen_rect.width / 4
        self.rect.centery = 3 * self.screen_rect.height / 4

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Prep the message of the button in a rendered image"""
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_color,
            self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_restart(self):
        """Draw the button on the screen"""
        self.screen.blit(self.msg_image, self.msg_image_rect)
        pygame.draw.rect(
            self.screen,
            self.text_color,
            self.rect,
            1  # width
        )
