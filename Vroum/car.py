"""Cars defintion"""
from __future__ import absolute_import

import math

import pygame

from utils import (
    blit_rotate_center,
    scale_img
)


class AbstractCar:
    """Parent class for the player and the oponent car

    Args:
            max_vel (int): maximum velocity of the car
            rotation_vel (int): maximum rotation velocity of the car
    """

    def __init__(self, max_vel: int, rotation_vel: int) -> None:
        self.max_vel = max_vel
        self.vel = 0
        self.acceleration = 0.1

        self.rotation_vel = rotation_vel
        self.angle = 0

        self.img = self.IMG
        self.x, self.y = self.START_POS

    def rotate(self, left: bool=False, right: bool=False) -> None:
        """Rotate the car in clockwise (right) or anticlockwise (left) momentum

        Args:
            left (bool, optional): Indicate if the move have to be anticlockwise. Defaults to False.
            right (bool, optional): Indicvate if the move have to be clockwise. Defaults to False.
        """
        if left:
            self.angle += self.rotation_vel

        if right:
            self.angle -= self.rotation_vel

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        
        self.y -= vertical
        self.x -= horizontal

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def draw(self, surface: pygame.surface) -> None:
        """Draw the car on the screen

        Args:
            surface (pygame.surface): The screen to draw on
        """
        blit_rotate_center(surface, self.img, (self.x, self.y), self.angle)



class PlayerCar(AbstractCar):
    """The car of the player"""
    IMG = scale_img(pygame.image.load('img/green-car.png'), 0.55)
    START_POS = (165, 200)
