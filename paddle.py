import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        # Define private screen width and height.
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Define shape and placing.
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=self.screen_width / 100)
        self.fillcolor("#E8A9A9")
        self.penup()
        self.speed("fastest")

        # Place paddle in the center bottom of the screen.
        self.reset_position()

        # Register mouse movement to move paddle
        self.screen = self.getscreen()
        self.ondrag(self.dragging)

    def dragging(self, x, y):
        """
        Function handles the paddle dragging movement based on mouse position.
        :param x: float.
        :param y: float.
        :return: None.
        """
        # Set the new x-coordinate to the current x-coordinate of the mouse.
        new_x = x
        # Check the x-coordinate within the screen boundaries.
        if new_x < -(self.screen_width / 2) + 70:
            new_x = -(self.screen_width / 2) + 70
        elif new_x > (self.screen_width / 2) - 80:
            new_x = (self.screen_width / 2) - 80

        self.goto(new_x, self.ycor())

    def reset_position(self):
        """
        Reset paddle position to screen center.
        :return: None.
        """
        self.goto(x=0, y=-(self.screen_height / 2) + 50)

    def get_x(self):
        return self.xcor()