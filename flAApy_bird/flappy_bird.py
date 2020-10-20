"""The main file of the game"""
from __future__ import absolute_import

import random
import sys
import time

import neat
import pygame

from bird import Bird
from settings import Settings


# pylint: disable=no-member
class FlappyGame:
    """The main class of the game"""
    def __init__(self) -> None:
        self.settings = Settings()

    def draw_window(self, win, bird):
        """quick draw of the windoiw"""
        win.blit(
            self.settings.bg_img,
            (0, 0)
        )
        bird.draw(win)
        pygame.display.update()

    def main(self):
        """mock main game"""
        bird = Bird(200, 200)
        win = pygame.display.set_mode((self.settings.win_width, self.settings.win_height))

        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            bird.move()
            self.draw_window(win, bird)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = FlappyGame()
    game.main()
