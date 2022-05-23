"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
# How to make the ball not stuck in the paddle?

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    # dx = graphics.get_ball_x()
    # dy = graphics.get_ball_y()
    graphics = BreakoutGraphics()
    life = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if life == 0 or graphics.score == 0:
            break
        else:
            if not graphics.can_click:
                graphics.ball.move(graphics.get_ball_x(), graphics.get_ball_y())
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    graphics.set_dx()
                if graphics.ball.y <= 0:
                    graphics.set_dy()
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    life -= 1
                    graphics.can_click = True
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) // 2,
                                        y=(graphics.window.height - graphics.ball.height) // 2)
                if graphics.ball_touch_brick():
                    graphics.set_dy()
                if graphics.ball_touch_paddle():
                    graphics.set_dy()
    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) // 2,
                        y=(graphics.window.height - graphics.ball.height) // 2)


if __name__ == '__main__':
    main()
