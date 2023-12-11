import unittest
from kivy.clock import Clock
from your_file_name import Game, Ball, Bat 

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.serve()
        Clock.schedule_interval(self.game.update, 1.0 / 60.0)

    def test_ball_movement(self):
        initial_position = self.game.ball.pos[:]
        self.game.update(1)
        new_position = self.game.ball.pos[:]
        self.assertNotEqual(initial_position, new_position)

    def test_ball_bounce(self):
        ball = Ball()
        ball.pos = (100, 100)
        ball.speed = (5, 0)
        bat = Bat()
        bat.pos = (ball.center_x, ball.center_y)

        initial_speed = ball.speed[:]
        bat.bounce(ball)
        new_speed = ball.speed[:]

        # Assert that the ball's speed changes after bouncing off the bat
        self.assertNotEqual(initial_speed, new_speed)

if __name__ == '__main__':
    unittest.main()
