"""The class to handle the ground and its movement"""
from __future__ import absolute_import

from settings import Settings


class Base:
    """The class for the ground."""

    def __init__(self, y) -> None:  # FIXME: should take the game object as parameter
        self.settings = Settings()  # FIXME: should be the settings of the game

        self.base_img = self.settings.base_img
        self.width = self.base_img.get_width()

        self.y_coord = y
        self.x_coord1 = 0
        self.x_coord2 = self.width

    def move(self):
        """Create the illusion of movement by moving the base"""
        self.x_coord1 -= self.settings.pipe_vel  # FIXME: proper velocity
        self.x_coord2 -= self.settings.pipe_vel

        if self.x_coord1 + self.width < 0:
            self.x_coord1 = self.x_coord2 + self.width

        if self.x_coord2 + self.width < 0:
            self.x_coord2 = self.x_coord1 + self.width

    def draw(self, win):
        """draw the bas to the game screen"""
        win.blit(self.base_img, (self.x_coord1, self.y_coord))
        win.blit(self.base_img, (self.x_coord2, self.y_coord))
