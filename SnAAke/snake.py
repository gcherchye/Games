"""Snake class"""
import pygame


class Snake():
    """Class to manage the player's snake"""

    def __init__(self, snake_game):
        """Initialize the snake and it's starting position"""
        # Settings and screen
        self.settings = snake_game.settings
        self.screen = snake_game.screen
        self.screen_rect = snake_game.screen.get_rect()

        # Speed and starting position
        self.speed = self.settings.snake_speed

        self.pos_x_idx = self.settings.nb_rows // 2
        self.pos_y_idx = self.settings.nb_rows // 2

        # Body variable
        self.element_size = self.settings.case_width - 2
        self.color = self.settings.snake_color
        self.body = []
        self.seg = []
        self.head = pygame.Rect(0, 0, 0, 0)

        # Direction flag
        self.direction = 'stop'

    def draw_snake(self):
        """Draw the snake on the screen"""
        self.seg = []

        # Draw the head
        self.head = pygame.Rect(
            self.pos_x_idx * self.settings.case_width + 1,
            self.pos_y_idx * self.settings.case_width + 1,
            self.element_size,
            self.element_size
        )

        pygame.draw.rect(
            self.screen,
            self.color,
            self.head
        )

        # Draw the rest of the body
        if len(self.body) > 0:
            for unit in self.body:
                segment = pygame.Rect(
                    unit[0] * self.settings.case_width + 1,
                    unit[1] * self.settings.case_width + 1,
                    self.element_size,
                    self.element_size
                )

                self.seg.append(segment)

                pygame.draw.rect(
                    self.screen,
                    self.color,
                    segment
                )

                self.seg.append(segment)

    def add_unit(self):
        """Add a unit to the snake

        If there is just the head, the new unit is added outside the screen
        and will be draw at the correct position after the next movement.
        If the body is not empty, it will create the new unit on the last
        element
        """
        if len(self.body) != 0:  # Check if just the head or not
            # Create the new element on the last
            index = len(self.body) - 1
            pos_x = self.body[index][0]
            pos_y = self.body[index][1]

            self.body.append([pos_x, pos_y])
        else:
            # Set the segment outside the screen, it will be redraw
            # at the correct place after
            self.body.append([1000, 1000])

    def move(self):
        """Trigger the flags movements"""
        for index in range(len(self.body) - 1, 0, -1):
            pos_x = self.body[index - 1][0]
            pos_y = self.body[index - 1][1]

            self.body[index] = [pos_x, pos_y]

        if len(self.body) > 0:
            self.body[0] = [self.pos_x_idx, self.pos_y_idx]
        if self.direction == 'up':
            self.pos_y_idx -= self.speed
        if self.direction == 'down':
            self.pos_y_idx += self.speed
        if self.direction == 'left':
            self.pos_x_idx -= self.speed
        if self.direction == 'right':
            self.pos_x_idx += self.speed

        self.boundary_move()

    def boundary_move(self):
        """Handle the mouvement outside the screen"""
        if self.direction == 'up' and self.pos_y_idx < 0:
            self.pos_y_idx = self.settings.nb_rows - 1
        elif self.direction == 'down' and \
                self.pos_y_idx > self.settings.nb_rows - 1:
            self.pos_y_idx = 0
        elif self.direction == 'left' and self.pos_x_idx < 0:
            self.pos_x_idx = self.settings.nb_rows - 1
        elif self.direction == 'right' and \
                self.pos_x_idx > self.settings.nb_rows - 1:
            self.pos_x_idx = 0

    def change_direction(self, direction):
        """Change the direction to tu input direction
        Only if not reverse

        Arguments:
            direction {string} -- the desired direction :
                        - up / down / left / right
        """
        if self.direction != 'down' and direction == 'up':
            self.direction = 'up'
        if self.direction != 'up' and direction == 'down':
            self.direction = 'down'
        if self.direction != 'left' and direction == 'right':
            self.direction = 'right'
        if self.direction != 'right' and direction == 'left':
            self.direction = 'left'

    def is_collision(self):
        """check for collision with itself"""
        for segment in self.seg:
            if self.head.colliderect(segment):
                return True
