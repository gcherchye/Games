"""Main script of the game"""
from __future__ import absolute_import

import math
import time

import pygame

from utils import (
    draw,
    scale_surf
)


# Load images
TRACK = pygame.image.load('img/track.png')
GRASS = pygame.transform.scale(
    pygame.image.load('img/grass.jpg'),
    (TRACK.get_width(), TRACK.get_height())
)
TRACK_BORDER = pygame.image.load('img/track-border.png')
FINISH = pygame.image.load('img/finish.png')
RED_CAR = scale_surf(pygame.image.load('img/red-car.png'), 0.55)
GREEN_CAR = scale_surf(pygame.image.load('img/green-car.png'), 0.55)

images = [
    (GRASS, (0, 0)),
    (TRACK, (0, 0))
]

# Pygame settings
WIN = pygame.display.set_mode((TRACK.get_width(), TRACK.get_height()))
pygame.display.set_caption('Vroum Vroum !!')

FPS = 60

# Main loop
RUN = True
clock = pygame.time.Clock()

while RUN:
    clock.tick(FPS)

    draw(WIN, images)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    pygame.display.update()

pygame.quit()
