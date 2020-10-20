"""flAApy bird game with NEAT"""
from __future__ import absolute_import

import pygame

from settings import Settings


class Bird:
    """Defining a bird"""

    def __init__(self, x, y) -> None:
        # Settings
        self.settings = Settings()
        self.x_coord = x
        self.y_coord = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y_coord
        self.img_count = 0
        self.img = self.settings.bird_imgs[0]

    def jump(self):
        """Make the bird jump"""
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y_coord

    def move(self):
        """Update the bird position"""
        self.tick_count += 1

        # Vertical velocity equation taking gravity into account
        displ = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

        # Ensure not to fall too fast
        if displ >= 16:
            displ = 16

        # Ensure not to jump too quick
        if displ < 0:
            displ -= 2

        # Changiing coordinate
        self.y_coord = self.y_coord + displ

        # Tilt the bird upward or downward based on displ and vertical positionnement
        if displ < 0 or self.y_coord < self.height + 50:
            if self.tilt < self.settings.max_rotation:
                self.tilt = self.settings.max_rotation
        else:
            if self.tilt > -90:  # Allow the bird to rotate to - 90 aka facing the ground
                self.tilt -= self.settings.rot_vel

    def draw(self, win):
        """Draw the bird on his new position and take in account the animation to make the
        bird flaps his wings, rotate the image to the tilt
        """
        self.img_count += 1

        if self.img_count < self.settings.animation_time:
            self.img = self.settings.bird_imgs[0]
        elif self.img_count < self.settings.animation_time * 2:
            self.img = self.settings.bird_imgs[1]
        elif self.img_count < self.settings.animation_time * 3:
            self.img = self.settings.bird_imgs[2]
        elif self.img_count < self.settings.animation_time * 4:
            self.img = self.settings.bird_imgs[1]
        elif self.img_count == self.settings.animation_time * 4 + 1:
            self.img = self.settings.bird_imgs[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.settings.bird_imgs[1]
            self.img_count = self.settings.animation_time * 2

        rotated = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated.get_rect(
            center=self.img.get_rect(
                topleft=(self.x_coord, self.y_coord)
            ).center
        )

        win.blit(
            rotated,
            new_rect.topleft
        )

    def get_mask(self):
        """Get the mask of the image"""
        return pygame.mask.from_surface(self.img)
