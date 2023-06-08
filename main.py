from brick import Brick
from score_board import Scoreboard
from turtle import Screen
from ball import Ball
from paddle import Paddle
import time


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

game_is_on = False


def handle_mouse_click(x, y):
    """
    Function handles the first mouse click for the user to start the game.
    :param x: float.
    :param y: float.
    :return: None
    """
    print(f"Clicked at ({x}, {y})")

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

    # Handle first click to start the game.
    global game_is_on
    game_is_on = False

    # Register the mouse click event handler
    screen.onclick(handle_mouse_click)

    while not game_is_on:
        screen.update()

    # Keyboard listening.
    screen.onkeypress(paddle.go_left, "Left")
    screen.onkeypress(paddle.go_right, "Right")
    screen.listen()


    # Start the game.
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()  # Update the screen manually because screen.tracer is set to 0.
        ball.move()  # Start ball movement.

        # ------------------- Ball Collisions ------------------- #
        # Check ball collision with top wall.
        if ball.ycor() > (SCREEN_HEIGHT / 2) - 20:
            ball.bounce_y()

        # Check ball collision with side walls.
        if ball.xcor() + 25 > (SCREEN_WIDTH / 2) or ball.xcor() - 20 < -(SCREEN_WIDTH / 2):
            ball.bounce_x()

        # Check ball collision with bottom wall.
        # TODO: LOSE POINT AND IMPROVE IF STATEMENT.
        if ball.ycor() < - (SCREEN_HEIGHT / 2) + 20:
            ball.bounce_y()

        # Check ball collision with a brick.
        for brick in bricks.bricks:
            if ball.distance(brick) < 30:
                if ball.ycor() > brick.ycor() + 10 or ball.ycor() < brick.ycor() - 10:
                    ball.bounce_y()  # Bounce the ball vertically.
                else:
                    ball.bounce_x()  # Bounce the ball horizontally.
                bricks.delete_brick(brick)
                game_is_on = False
                break
                # TODO: Add point

        # Check ball collision with the paddle.
        if ball.paddle_collision(paddle):
            ball.bounce_y()

    screen.exitonclick()


if __name__ == "__main__":
    main()
