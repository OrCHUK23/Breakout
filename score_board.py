from turtle import Turtle

ALIGNMENT = "center"
POINTS_FONT = ("Myriad Pro Black", 40, "bold")
LABEL_FONT = ("Myriad Pro Black", 15, "bold")
WIN_FONT = ("Myriad Pro Black", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.lives = 100
        self.bricks = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Function handles scoreboard showing.
        :return: None.
        """
        self.clear()

        # Draw bricks state.
        self.goto(-270, 180)
        self.write("Bricks", align=ALIGNMENT, font=LABEL_FONT)
        self.goto(-270, 120)
        self.write(self.bricks, align=ALIGNMENT, font=POINTS_FONT)

        # Draw lives remaining state.
        self.goto(270, 180)
        self.write("Life", align=ALIGNMENT, font=LABEL_FONT)
        self.goto(270, 120)
        self.write(self.lives, align=ALIGNMENT, font=POINTS_FONT)

    def add_brick_point(self):
        """
        Function handles bricks that got broken.
        :return: None.
        """
        self.bricks += 1
        self.update_scoreboard()

    def reduce_life(self):
        """
        Function reduces remaining life of the player.
        :return: None.
        """
        self.lives -= 1
        self.update_scoreboard()

    def show_win_message(self):
        """
        Function handles win message if there are no more bricks.
        :return: None.
        """
        self.goto(0, 0)
        self.color("turquoise")
        self.write("You win!", align=ALIGNMENT, font=WIN_FONT)