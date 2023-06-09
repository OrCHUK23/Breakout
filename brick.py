from turtle import Turtle, Screen
import colorsys
import random

BRICK_WIDTH = 40
BRICK_HEIGHT = 20
STARTING_ROW = 7  # Number of bricks in each row.
STARTING_POSITION_X = -150
STARTING_POSITION_Y = 30
BRICK_GAP = 10  # Gap between bricks


class Brick(Turtle):
    def __init__(self):
        """
        Initialization of the bricks.
        """
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        """
        Function handles the creation of the bricks.
        :return: None.
        """
        for row in range(STARTING_ROW):
            for col in range(STARTING_ROW):
                x = STARTING_POSITION_X + (BRICK_WIDTH + BRICK_GAP) * col
                y = STARTING_POSITION_Y + (BRICK_HEIGHT + BRICK_GAP) * row
                brick_segment = Turtle("square")
                brick_segment.shapesize(stretch_wid=1, stretch_len=2)
                brick_segment.penup()
                brick_segment.color(self.__generate_random_color())
                brick_segment.speed("fastest")
                brick_segment.goto(x, y)
                self.bricks.append(brick_segment)

    def delete_brick(self, brick):
        """
        Function handles deletion of a brick.
        :param brick: Turtle object.
        :return: None.
        """
        brick.goto(10000, 10000)
        self.bricks.remove(brick)

    def delete_all_bricks(self):
        """
        Function deletes all bricks in the window.
        :return: None.
        """
        for brick in self.bricks:
            brick.goto(10000, 10000)

    @staticmethod
    def __generate_random_color():
        """
        Function generates random color for a brick.
        :return: str.
        """
        hue_range = 10  # Range of hue variation (0-360)
        base_hue = 26  # Base hue for the bricks (corresponding to #EEE2DE)
        min_hue = (base_hue - hue_range + 360) % 360
        max_hue = (base_hue + hue_range) % 360

        if min_hue > max_hue:
            hue = random.randint(max_hue, min_hue)
        else:
            hue = random.randint(min_hue, max_hue)

        saturation = random.uniform(0.1, 0.9)  # Random saturation value (0.6-1.0)
        value = random.uniform(0.6, 0.9)  # Random value/brightness value (0.8-1.0)

        r, g, b = colorsys.hsv_to_rgb(hue / 360, saturation, value)
        hex_color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
        return hex_color

    @staticmethod
    def __hsv_to_rgb(hue, saturation, value):
        """
        Function converts HSV (Hue, Saturation, Value) color representation to RGB color representation.
        :param hue: Hue value in the range 0-360.
        :param saturation: Saturation value in the range 0.0-1.0.
        :param value: Value (brightness) value in the range 0.0-1.0.
        :return: RGB color tuple as (red, green, blue), each component ranging from 0-255.
        """
        rgb = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(hue / 360, saturation, value))
        return rgb



