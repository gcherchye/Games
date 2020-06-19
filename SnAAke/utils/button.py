"""Classes to handle buttons"""
import pygame


class Buttons:
    """The overall class to handle buttons"""

    def __init__(self, snake_game, msg):
        """Initialize the buttons and its parameters

        Args:
            snake_game (object): The instance of the game
            msg (str): The message to display on the button
        """
        # Screen settings
        self.window = snake_game.window
        self.screen_rect = snake_game.screen

        # Size and font parameters
        self.width, self.height = 150, 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_color = snake_game.settings.back_color
        self.text_color = snake_game.settings.snake_color
        self.font = pygame.font.SysFont(None, 48)

        # Prep the button image
        self._prep_message(msg)


    def _prep_message(self, msg):
        """Prep the message into a rendered image

        Args:
            msg (str): the message to display on the button
        """
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_color,
            self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the button on the screen"""
        self.window.fill(self.button_color, self.rect)
        self.window.blit(self.msg_image, self.msg_image_rect)
        pygame.draw.rect(
            self.window,
            self.text_color,
            self.rect,
            1  # width
        )


class PlayButton(Buttons):
    """The play button"""

    def __init__(self, snake_game, msg):
        super().__init__(snake_game, msg)

        # Set the position of the button
        self.rect.center = self.screen_rect.center

        # Prep the message at the correct place
        self._prep_message(msg)


class ExitButton(Buttons):
    """The Exit buttons"""

    def __init__(self, snake_game, msg):
        super().__init__(snake_game, msg)

        # Set the position of the button
        self.rect.centerx = self.screen_rect.width / 4
        self.rect.centery = 3 * self.screen_rect.height / 4

        # Prep the message at the correct place
        self._prep_message(msg)


class RestartButton(Buttons):
    """The Restart button"""

    def __init__(self, snake_game, msg):
        super().__init__(snake_game, msg)

        # Set the position of the button
        self.rect.centerx = 3 * self.screen_rect.width / 4
        self.rect.centery = 3 * self.screen_rect.height / 4

        # Prep the message at the correct place
        self._prep_message(msg)
