import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x_surface, y_surface):
        # Turtle settings.
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()

        # Movement settings.
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.009

        # Position settings.
        self.ball_x_surface = x_surface  # First x pos of the ball.
        self.ball_y_surface = y_surface  # First y pos of the ball.
        self.reset_position()

    def move(self):
        """
        Function handles ball's constant movement.
        :return: None.
        """
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        """
        Function handles change of ball direction on y line.
        :return: None.
        """
        self.y_move *= - 1

    def bounce_x(self):
        """
        Function handles change of ball direction on x line.
        :return: None.
        """
        self.x_move *= - 1

    def paddle_collision(self, paddle):
        """
        Check ball collision with the paddle.
        :param paddle: Paddle object
        :return: bool.
        """
        ball_x = self.xcor()
        ball_y = self.ycor()
        paddle_x = paddle.xcor()
        paddle_y = paddle.ycor()

        # Convert paddle size to pixels
        paddle_width = paddle.shapesize()[1] * 20
        paddle_height = paddle.shapesize()[0] * 20

        return (paddle_y - paddle_height / 2 <= ball_y <= paddle_y + paddle_height / 2
                and paddle_x - paddle_width / 2 <= ball_x <= paddle_x + paddle_width / 2)

    def reset_position(self):
        """
        Reset the ball position.
        :return: None.
        """
        self.goto(self.ball_x_surface, self.ball_y_surface + 20)
