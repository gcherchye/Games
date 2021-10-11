"""Utilitary functions"""
from __future__ import absolute_import

import pygame


def draw(surface: pygame.Surface, images: list[tuple[pygame.Surface, tuple[int, int]]]) -> None:
    """Draw images on the surface at their deesignated position

    Args:
        surface (pygame.Surface): The surface to draw on
        images (list[tuple[pygame.Surface, tuple[int, int]]]): The list of the image to draw, and
        their postitions
    """
    for img, position in images:
        surface.blit(img, position)

def scale_surf(surface: pygame.Surface, factor: float) -> pygame.Surface:
    """Apply a size transformation factor to an image

    Args:
        surface (pygame.Surface): The surface to modify
        factor (float): The increase/decrease factor

    Returns:
        pygame.Surface: The resulting image
    """
    size = round(surface.get_width() * factor), round(surface.get_height() * factor)

    return pygame.transform.scale(surface, size)
