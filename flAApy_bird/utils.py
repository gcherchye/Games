"""Misc function & stuff to be used in the different classes of the game"""
from __future__ import absolute_import

import os

import pygame


# Images
def load_image(folder: str, name: str, ext: str) -> pygame.Surface:
    """Load an image stored in a folder inside the working directory and double the mesurments

    Args:
        folder (str): the name of the folder
        name (str): the name of the image file
        ext (str): the extension of the image file (without the '.')

    Returns:
        pygame.Surface: The image loaded as a pygame Surface
    """
    return pygame.transform.scale2x(pygame.image.load(os.path.join(folder, name + '.' + ext)))
