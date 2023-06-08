from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        # Define private screen width and height.
        self.__screen_width = screen_width
        self.__screen_height = screen_height

        # Define shape and placing.
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=self.__screen_width / 100)
        self.fillcolor("#B31312")
        self.penup()
        self.speed("fastest")

        # Place paddle in the center bottom of the screen.
        self.goto(x=0, y=-(self.__screen_height / 2) + 50)

    def go_left(self):
        """
        Function handles the paddle left movement.
        :return: None
        """
        new_x = self.xcor() - 30
        if self.__check_left_wall(self.__screen_width):
            self.goto(new_x, self.ycor())

    def go_right(self):
        """
        Function handles the paddle right movement.
        :return: None
        """
        new_x = self.xcor() + 30
        if self.__check_right_wall(self.__screen_width):
            self.goto(new_x, self.ycor())

    def __check_left_wall(self, screen_width):
        """
        Private function to handle collision with left wall.
        :param screen_width: int.
        :return: bool.
        """
        return self.xcor() > -(screen_width / 2) + 70

    def __check_right_wall(self, screen_width):
        """
        Private function to handle collision with left wall.
        :param screen_width: int.
        :return: bool.
        """
        return self.xcor() < (screen_width / 2) - 80
