from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x_surface, y_surface):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08
        self.goto(x_surface, y_surface + 20)

    def move(self):
        """
        Function handles ball's constant movement.
        :return: None.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Function handles change of ball direction on y line.
        :return: None
        """
        self.y_move *= - 1

    def bounce_x(self):
        """
        Function handles change of ball direction on x line.
        :return: None
        """
        self.x_move *= - 1
        # self.move_speed *= 0.8

    def paddle_collision(self, paddle):
        """
        Function handles the ball collision with the paddle.
        :param paddle: Turtle.
        :return: bool.
        """
        ball_left = self.xcor() - 10  # Assuming the ball has a width of 20
        ball_right = self.xcor() + 10
        ball_top = self.ycor() + 10
        ball_bottom = self.ycor() - 10

        paddle_left = paddle.xcor() - (paddle.shapesize()[1] * 10) / 2  # Calculate paddle width based on shape size
        paddle_right = paddle.xcor() + (paddle.shapesize()[1] * 10) / 2
        paddle_top = paddle.ycor() + (paddle.shapesize()[0] * 10) / 2  # Calculate paddle height based on shape size
        paddle_bottom = paddle.ycor() - (paddle.shapesize()[0] * 10) / 2

        return not (ball_left > paddle_right or ball_right < paddle_left or
                    ball_top < paddle_bottom or ball_bottom > paddle_top + 10)

    def reset_position(self):
        """
        Reset ball position.
        :return: None.
        """
        self.goto(0, 0)
        self.move_speed = 0.1