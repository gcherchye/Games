"""Snake class"""
import pygame


class Snake():
    """Class to manage the player's snake"""

    def __init__(self, snake_game):
        """Initialize the snake and it's starting position"""
        # The instance of the game
        self.snake_game = snake_game

        # Speed and starting position
        self.speed = self.snake_game.settings.snake_speed
        self.pos_incr = 0

        self.pos_x_idx = self.snake_game.settings.nb_rows_x // 2
        self.pos_y_idx = self.snake_game.settings.nb_rows_y // 2

        # Loading images
        self.head_up = pygame.transform.scale(
            pygame.image.load(r'utils\Images\head.png'),
            (self.snake_game.settings.element_size, self.snake_game.settings.element_size)
        )
        self.body_image = pygame.transform.scale(
            pygame.image.load(r'utils\Images\body.png'),
            (self.snake_game.settings.element_size, self.snake_game.settings.element_size)
        )

        # Transforming the head for other direction
        self.head_down = pygame.transform.rotate(
            self.head_up,
            180
        )
        self.head_right = pygame.transform.rotate(
            self.head_up,
            -90
        )
        self.head_left = pygame.transform.rotate(
            self.head_up,
            90
        )

        # Retreiving rect of images and setting starting position
        self.head_rect = self.head_up.get_rect()
        self.head_rect.x = self.pos_x_idx * self.snake_game.settings.case_width + 2
        self.head_rect.y = self.pos_y_idx * self.snake_game.settings.case_width + 2

        self.body_elem_rect = self.body_image.get_rect()

        # Setting body variables
        self.body = []
        self.seg = []

        # Flags
        self.direction = 'stop'
        self.collision = False
        self.moved = False
        self.move_recorded = False

    def draw_snake(self):
        """Draw the snake on the screen"""
        # Draw the head
        self._draw_head()

        # Draw the rest of the body
        if len(self.body) > 0:
            self._draw_body()

    def _draw_head(self):
        """Draw the head of the snake on the screen"""
        self.head_rect.x = self.pos_x_idx * self.snake_game.settings.case_width + 2
        self.head_rect.y = self.pos_y_idx * self.snake_game.settings.case_width + 2

        if self.direction in ('stop', 'up'):
            self.snake_game.window.blit(self.head_up, self.head_rect)
        elif self.direction == 'right':
            self.snake_game.window.blit(self.head_right, self.head_rect)
        elif self.direction == 'left':
            self.snake_game.window.blit(self.head_left, self.head_rect)
        elif self.direction == 'down':
            self.snake_game.window.blit(self.head_down, self.head_rect)

    def _draw_body(self):
        """Draw the body on the screen"""
        self.seg = []

        for unit in self.body:
            segment = pygame.Rect(
                unit[0] * self.snake_game.settings.case_width + 2,
                unit[1] * self.snake_game.settings.case_width + 2,
                self.snake_game.settings.element_size,
                self.snake_game.settings.element_size
            )

            self.snake_game.window.blit(
                self.body_image,
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
            # at the correct place after the mouvement by the if bloc
            self.body.append([1000, 1000])

    def move(self, delta_t):
        """Move the snake and handle boundary teleportation

        Args:
            delta_t (float): the interval of time between each frame [ms]
        """
        self.calc_new_position(delta_t)
        self.boundary_move()

    def calc_new_position(self, delta_t):
        """Increment the deplacement flag according to the snake speed and calc the new position
        of the snake according to it.

        Args:
            delta_t (float): the interval of time between each frame [ms]
        """
        self.moved = False
        self.pos_incr += self.speed * (delta_t / 1000)

        if round(self.pos_incr) != 0:
            for index in range(len(self.body) - 1, 0, -1):
                pos_x = self.body[index - 1][0]
                pos_y = self.body[index - 1][1]

                self.body[index] = [pos_x, pos_y]

            if len(self.body) > 0:
                self.body[0] = [self.pos_x_idx, self.pos_y_idx]

            if self.direction == 'up':
                self.pos_y_idx -= round(self.pos_incr)
            elif self.direction == 'down':
                self.pos_y_idx += round(self.pos_incr)
            elif self.direction == 'left':
                self.pos_x_idx -= round(self.pos_incr)
            elif self.direction == 'right':
                self.pos_x_idx += round(self.pos_incr)

            self.moved = True
            self.move_recorded = False

            self.pos_incr = 0

    def boundary_move(self):
        """Handle the mouvement outside the filed"""
        if self.direction == 'up' and self.pos_y_idx < 1:
            self.pos_y_idx = self.snake_game.settings.nb_rows_y - 4
        elif self.direction == 'down' and \
                self.pos_y_idx > self.snake_game.settings.nb_rows_y - 4:
            self.pos_y_idx = 1
        elif self.direction == 'left' and self.pos_x_idx < 1:
            self.pos_x_idx = self.snake_game.settings.nb_rows_x - 2
        elif self.direction == 'right' and \
                self.pos_x_idx > self.snake_game.settings.nb_rows_x - 2:
            self.pos_x_idx = 1

    def change_direction(self, direction):
        """Change the direction to the input direction if not reverse

        Args:
            direction (str): the desired recorded based on the keyboard key pressed
                        - up / down / left / right
        """
        if self.direction != 'down' and direction == 'up':
            self.direction = 'up'
        elif self.direction != 'up' and direction == 'down':
            self.direction = 'down'
        elif self.direction != 'left' and direction == 'right':
            self.direction = 'right'
        elif self.direction != 'right' and direction == 'left':
            self.direction = 'left'

        self.move_recorded = True

    def is_self_collision(self):
        """check for collision with itself"""
        for segment in self.seg:
            if self.head_rect.colliderect(segment):
                self.collision = True

        return self.collision

    def reset_snake(self):
        """Reset the snake parameter to default if game over"""
        self.body = []
        self.pos_x_idx = self.snake_game.settings.nb_rows_x // 2
        self.pos_y_idx = self.snake_game.settings.nb_rows_y // 2

        self.direction = 'stop'
        self.collision = False
        self.moved = False
        self.move_recorded = False
