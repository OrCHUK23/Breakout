from score_board import Scoreboard
from brick import Brick
from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

# Screen width and height.
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Global bool for game status.
game_is_on = False


def handle_mouse_click(x, y):
    """
    Function handles the first mouse click for the user to start the game.
    :param x: float.
    :param y: float.
    :return: None
    """
    global game_is_on
    game_is_on = True


def main():
    # Create and define the screen object.
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("#2B2A4C")
    screen.title("Breakout")
    screen.tracer(0)  # Make animation off and update it manually by screen.update().

    # Game objects.
    paddle = Paddle(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
    ball = Ball(paddle.xcor(), paddle.ycor())
    bricks = Brick()
    score_board = Scoreboard()

    # Handle first click to start the game.
    global game_is_on
    game_is_on = False

    # Register the mouse click event handler.
    screen.onclick(handle_mouse_click)

    while not game_is_on:
        screen.update()

    # Start the game.
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()  # Update the screen manually because screen.tracer is set to 0.
        ball.move()  # Start ball movement.

        if bricks.bricks:
            # Check ball collision with a brick.
            for brick in bricks.bricks:
                if ball.distance(brick) < 30:
                    score_board.add_brick_point()
                    if ball.ycor() > brick.ycor() + 10 or ball.ycor() < brick.ycor() - 10:
                        ball.bounce_y()  # Bounce the ball vertically.
                    else:
                        ball.bounce_x()  # Bounce the ball horizontally.
                    bricks.delete_brick(brick)

        # No more bricks
        else:
            game_is_on = False
            score_board.show_win_message()

        # Check ball collision with top wall.
        if ball.ycor() > (SCREEN_HEIGHT / 2) - 20:
            ball.bounce_y()

        # Check ball collision with side walls.
        if ball.xcor() + 25 > (SCREEN_WIDTH / 2) or ball.xcor() - 20 < -(SCREEN_WIDTH / 2):
            ball.bounce_x()

        # Check ball collision with bottom wall.
        if ball.ycor() < - (SCREEN_HEIGHT / 2) + 20:
            # Reduce life
            score_board.reduce_life()
            ball.reset_position(paddle.xcor(), paddle.ycor())
            # Check if game lost.
            if score_board.lives == 0:
                game_is_on = False

        # Check ball collision with the paddle.
        if ball.paddle_collision(paddle):
            ball.bounce_y()

    screen.exitonclick()


if __name__ == "__main__":
    main()