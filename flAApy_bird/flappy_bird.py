"""The main file of the game"""
from __future__ import absolute_import

import sys
import time

import neat
import pygame

from base import Base
from bird import Bird
from pipe import Pipe
from settings import Settings

pygame.font.init()

STAT_FONT = pygame.font.SysFont('comicsans', 50)

# pylint: disable=no-member
class FlappyGame:
    """The main class of the game"""
    def __init__(self) -> None:
        self.settings = Settings()

    def draw_window(self, win, bird, pipes, base, score):
        """quick draw of the windoiw"""
        win.blit(
            self.settings.bg_img,
            (0, 0)
        )

        for pipe in pipes:
            pipe.draw(win)

        text = STAT_FONT.render('Score : ' + str(score), True, (255, 255, 255))
        win.blit(text, (self.settings.win_width - 10 - text.get_width(), 10))

        base.draw(win)

        bird.draw(win)

        pygame.display.update()

    def main(self):
        """mock main game"""
        bird = Bird(230, 350)
        base = Base(730)
        pipes = [Pipe(600)]
        win = pygame.display.set_mode((self.settings.win_width, self.settings.win_height))

        clock = pygame.time.Clock()

        score = 0

        run = True
        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #bird.move()

            remove_pipe = []  # TODO : get that in a function
            add_pipe = False
            for pipe in pipes:
                if pipe.collide(bird):
                    pass  # TODO: game over

                if pipe.x_coord + pipe.pipe_top.get_width() < 0:
                    remove_pipe.append(pipe)

                if not pipe.passed and pipe.x_coord < bird.x_coord:
                    pipe.passed = True
                    add_pipe = True

                pipe.move()

            if add_pipe:
                score += 1
                pipes.append(Pipe(600))

            for trash in remove_pipe:
                pipes.remove(trash)

            if bird.y_coord + bird.img.get_height() >= 730:  # FIXME: Variable the 730
                pass  # TODO: game over


            base.move()
            self.draw_window(win, bird, pipes, base, score)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = FlappyGame()
    game.main()
