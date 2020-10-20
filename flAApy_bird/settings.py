"""overall setting for the flappy bird"""
from __future__ import absolute_import

from utils import (
    load_image
)


class Settings:
    """All settings for the game"""
    def __init__(self) -> None:
        # Window settings
        self.win_width = 500
        self.win_height = 800

        # Game settings
        self.base_img = load_image('Images', 'base', 'png')
        self.bg_img = load_image('Images', 'bg', 'png')
        self.pipe_img = load_image('Images', 'pipe', 'png')

        # Bird settings
        self.max_rotation = 25
        self.rot_vel = 20
        self.animation_time = 5

        self.bird_imgs = [
            load_image('Images', 'bird1', 'png'),
            load_image('Images', 'bird2', 'png'),
            load_image('Images', 'bird3', 'png')
        ]
