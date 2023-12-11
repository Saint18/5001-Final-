from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import ObjectProperty

from kivy.vector import Vector
from kivy.clock import Clock


class Bat(Widget):
    score = NumericProperty(0)

    def bounce(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.speed
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            speed = bounced * 1.15
            ball.speed = speed.x, speed.y + offset


"""class that initiates the bats on the screen and the score to 0.
The function is what tells the ball to bounce of the bat the limit of the screen
The speed of the ball increases by 15% after every bounce."""


class Ball(Widget):
    speed_x = NumericProperty(0)
    speed_y = NumericProperty(0)
    speed = ReferenceListProperty(speed_x, speed_y)

    def move(self):
        self.pos = Vector(*self.speed) + self.pos


"""Class Ball is what allows the ball to move on the screen. 
The function uses the speed variable to increase speed by 15%."""


class Game(Widget):
    ball = ObjectProperty(None)
    first_player = ObjectProperty(None)
    second_player = ObjectProperty(None)

    def serve(self, speed=(4, 0)):
        self.ball.center = self.center
        self.ball.speed = speed

    def update(self, dt):
        self.ball.move()

        self.first_player.bounce(self.ball)
        self.second_player.bounce(self.ball)

        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:
            self.second_player.score += 1
            self.serve(speed=(4, 0))
        if self.ball.right > self.width:
            self.first_player.score += 1
            self.serve(speed=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.first_player.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.second_player.center_y = touch.y


"""Game class is what glues all of the functions and the YML file together. 
starts the game using the the serve function that kicks off the ball in the center 
with initial speed. Initializes the first player and second player bats. 
The update function is what allows the ball to know the limit of the screen 
and where to bounce off of. The touch function is what allows the ball to bounce
off of the edge of the screen and the bats."""


class PongApp(App):
    def build(self):
        game = Game()
        game.serve()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


"""Class PongApp and function build are the commands that start the game. 
We begin with the serve and calling Class Game. Serves ball and runs program. """

if __name__ == '__main__':
    PongApp().run()
