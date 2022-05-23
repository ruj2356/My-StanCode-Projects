"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        # Center a filled ball in the graphical window
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        # Draw bricks

        # Paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2,
                            y=(window_height - paddle_height - paddle_offset))
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Ball
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - ball_radius * 2) // 2, y=(window_height - ball_radius * 2) // 2)

        # Ball speed
        self.__dx = 0
        self.__dy = 0

        self.ball_velocity()

        # Brick score
        """
        Number of bricks that remains
        """
        self.score = brick_rows * brick_cols

        # Bricks
        """
        Create bricks
        """
        for i in range(0, brick_cols):
            for j in range(0, brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j // 2 == 0:
                    self.brick.fill_color = 'red'
                elif j // 2 == 1:
                    self.brick.fill_color = 'orange'
                elif j // 2 == 2:
                    self.brick.fill_color = 'yellow'
                elif j // 2 == 3:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=i * (brick_width + brick_spacing),
                                y=j * (brick_height + brick_spacing) + brick_offset)

        onmouseclicked(self.ball_start_move)
        self.can_click = True

    # Paddle move
    def paddle_move(self, mouse):
        """
        The paddle will follow user's mouse
        :param mouse: User's mouse
        :return: None
        """
        if self.paddle.width / 2 < mouse.x < self.window.width - self.paddle.width / 2:
            self.paddle.x = mouse.x - self.paddle.width / 2
        elif mouse.x < self.paddle.width / 2:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width - self.paddle.width

    # Ball move
    def ball_start_move(self, mouse):
        """
        The ball will start moving
        :param mouse: User's mouse
        :return: None
        """
        self.can_click = False
        onmousemoved(self.paddle_move)

    # Ball move speed
    def ball_velocity(self):
        """
        Determines ball velocity
        :return: None
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Getter ball x, y
    def get_ball_x(self):
        return self.__dx

    def get_ball_y(self):
        return self.__dy

    # Setter ball x, y
    def set_dy(self):
        self.__dy *= -1

    def set_dx(self):
        self.__dx *= -1

    # When ball touch brick
    def ball_touch_brick(self):
        """
        Determine when the ball touches bricks
        :return: bool
        """
        for i in range(self.ball.x, (self.ball.x + self.ball.width + 1), self.ball.width):
            for j in range(self.ball.y, (self.ball.y + self.ball.height + 1), self.ball.height):
                obj = self.window.get_object_at(i, j)
                if obj is not None:
                    if obj is not self.paddle:
                        self.window.remove(obj)
                        self.score -= 1
                        return True

    # When ball touch paddle
    def ball_touch_paddle(self):
        """
        Determine when the ball touches the paddle
        :return: bool
        """
        for i in range(self.ball.x, (self.ball.x + self.ball.width + 1), self.ball.width):
            for j in range(self.ball.y, (self.ball.y + self.ball.height + 1), self.ball.height):
                obj = self.window.get_object_at(i, j)
                if obj is not None:
                    if obj is self.paddle and self.__dy > 0:
                        return True
