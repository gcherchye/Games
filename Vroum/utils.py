"""Utilitary functions"""
from __future__ import absolute_import

import pygame


def draw(
    surface: pygame.Surface,
    images: list[tuple[pygame.Surface, tuple[int, int]]],
    player_car
) -> None:
    """Draw images on the surface at their designated position

    Args:
        surface (pygame.Surface): The surface to draw on
        images (list[tuple[pygame.Surface, tuple[int, int]]]): The list of the image to draw, and
        their postitions
    """
    for img, position in images:
        surface.blit(img, position)

    player_car.draw(surface)
    pygame.display.update()


def scale_img(image: pygame.Surface, factor: float) -> pygame.Surface:
    """Apply a size transformation factor to an image

    Args:
        image (pygame.Surface): The image to modify
        factor (float): The increase/decrease factor

    Returns:
        pygame.Surface: The resulting image
    """
    size = round(image.get_width() * factor), round(image.get_height() * factor)

    return pygame.transform.scale(image, size)


def blit_rotate_center(
    surface: pygame.surface,
    image: pygame.surface,
    top_left: tuple,
    angle: int
) -> None:
    """Rotate an image by its center and draw it on a surface

    Args:
        surface (pygame.surface): The surface to draw on
        image (pygame.surface): The image to rotate and draw
        top_left (tuple): The position of the topleft corner of the image
        angle (int): The rotation angle
    """
    rotated = pygame.transform.rotate(image, angle)
    new_rect = rotated.get_rect(center=image.get_rect(topleft=top_left).center)

    surface.blit(rotated, new_rect.topleft)
