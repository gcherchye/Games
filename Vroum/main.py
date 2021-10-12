"""Main script of the game"""
from __future__ import absolute_import

import pygame

from car import PlayerCar
from utils import (
    draw,
    scale_img
)


# Load images
TRACK = pygame.image.load('img/track.png')
GRASS = pygame.transform.scale(
    pygame.image.load('img/grass.jpg'),
    (TRACK.get_width(), TRACK.get_height())
)
TRACK_BORDER = pygame.image.load('img/track-border.png')
FINISH = pygame.image.load('img/finish.png')
RED_CAR = scale_img(pygame.image.load('img/red-car.png'), 0.55)

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
player_car = PlayerCar(4, 4)

while RUN:
    clock.tick(FPS)

    draw(WIN, images, player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    MOVED = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_z]:
        MOVED = True
        player_car.move_forward()

    if not MOVED:
        player_car.reduce_speed()


pygame.quit()
