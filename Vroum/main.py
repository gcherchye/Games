"""Main script of the game"""
from __future__ import absolute_import

import math
import time

import pygame


# Load images
GRASS = pygame.image.load('img/grass.jpg')
TRACK = pygame.image.load('img/track.png')
TRACK_BORDER = pygame.image.load('img/track-border.png')
FINISH = pygame.image.load('img/finish.png')
RED_CAR = pygame.image.load('img/red-car.png')
GREEN_CAR = pygame.image.load('img/green-car.png')

# Pygame settings
WIN = pygame.display.set_mode((TRACK.get_width(), TRACK.get_height()))
pygame.display.set_caption('Vroum Vroum !!')

FPS = 60

# Main loop
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()