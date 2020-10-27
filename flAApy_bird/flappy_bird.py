"""The main file of the game"""
from __future__ import absolute_import

import os
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
GEN = 0

# pylint: disable=no-member
class FlappyGame:
    """The main class of the game"""
    def __init__(self) -> None:
        self.settings = Settings()

    def draw_window(self, win, birds, pipes, base, score, gen):
        """quick draw of the windoiw"""
        win.blit(
            self.settings.bg_img,
            (0, 0)
        )

        for pipe in pipes:
            pipe.draw(win)

        score_text = STAT_FONT.render('Score : ' + str(score), True, (255, 255, 255))
        win.blit(score_text, (self.settings.win_width - 10 - score_text.get_width(), 10))

        gen_text = STAT_FONT.render('Generation : ' + str(gen), True, (255, 255, 255))
        win.blit(gen_text, (10, 10))

        base.draw(win)

        for bird in birds:
            bird.draw(win)

        pygame.display.update()

    def main(self, genomes, config):
        """mock main game"""
        global GEN
        GEN += 1
        nets = []
        genome = []
        birds = []

        for _, gen in genomes:
            net = neat.nn.FeedForwardNetwork.create(gen, config)
            nets.append(net)

            birds.append(Bird(230, 350))

            gen.fitness = 0
            genome.append(gen)

        base = Base(730)
        pipes = [Pipe(600)]
        win = pygame.display.set_mode((self.settings.win_width, self.settings.win_height))

        clock = pygame.time.Clock()

        score = 0

        run = True
        while run:
            clock.tick(100000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

            pipe_idx = 0
            if len(birds) > 0:
                if len(pipes) > 1 \
                and birds[0].x_coord > pipes[0].x_coord + pipes[0].pipe_top.get_width():
                    pipe_idx = 1
            else:
                run = False
                break  # TODO: get rid of that uglyness

            for idx, bird in enumerate(birds):
                bird.move()
                genome[idx].fitness += 0.1

                output = nets[idx].activate((
                    bird.y_coord,
                    abs(bird.y_coord - pipes[pipe_idx].top),
                    abs(bird.y_coord - pipes[pipe_idx].bottom)
                ))

                if output[0] > 0.5:
                    bird.jump()

            remove_pipe = []  # TODO : get that in a function
            add_pipe = False
            for pipe in pipes:
                for idx, bird in enumerate(birds):
                    if pipe.collide(bird):
                        genome[idx].fitness -= 1
                        birds.pop(idx)
                        nets.pop(idx)
                        genome.pop(idx)

                    if not pipe.passed and pipe.x_coord < bird.x_coord:
                        pipe.passed = True
                        add_pipe = True

                if pipe.x_coord + pipe.pipe_top.get_width() < 0:
                    remove_pipe.append(pipe)

                pipe.move()

            if add_pipe:
                score += 1

                for gen in genome:
                    gen.fitness += 5

                pipes.append(Pipe(600))

            for trash in remove_pipe:
                pipes.remove(trash)

            for idx, bird in enumerate(birds):
                if bird.y_coord + bird.img.get_height() >= 730 \
                or bird.y_coord < 0:  # FIXME: Variable the 730
                    birds.pop(idx)
                    nets.pop(idx)
                    genome.pop(idx)

            base.move()
            self.draw_window(win, birds, pipes, base, score, GEN)

    def run(self, config_path):
        config = neat.config.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            config_path
        )

        population = neat.Population(config)

        population.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        population.add_reporter(stats)

        winner = population.run(self.main, 50)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    neat_config_path = os.path.join(local_dir, 'neat_config.txt')

    game = FlappyGame()
    game.run(neat_config_path)
