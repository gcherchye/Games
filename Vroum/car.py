"""Cars defintion"""
from __future__ import absolute_import


class AbstractCar:
    """Parent class for the player and the oponent car

    Args:
            max_vel (int): maximum velocity of the car
            rotation_vel (int): maximum rotation velocity of the car
    """

    def __init__(self, max_vel: int, rotation_vel: int) -> None:
        self.max_vel = max_vel
        self.vel = 0

        self.rotation_vel = rotation_vel
        self.angle = 0

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


class PlayerCar(AbstractCar):
    """The car of the player"""
