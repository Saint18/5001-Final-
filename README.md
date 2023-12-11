# 5001-Final-
Final Project Report

Student Name: Gabriel Crito
Github Username: Saint18
Semester: Fall 
Course: 5001 
Description

General overview of the project, what you did, why you did it, etc.
I chose to do a video game recreation of pong. I chose to do it because I wanted to get an introduction to creating video games and learn about the type of skills you need to be successful. 
Key Features

Highlight some key features of this project that you want to show off/talk about/focus on.
The organization of the project into classes and the conciseness of the code is a key feature to focus on. 
Guide

How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features.
The code will run the pong game. 
Installation Instructions

If we wanted to run this project locally, what would we need to do? If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run pip install -r requirements.txt or something similar.
Make sure to pip install kivy to run the program. 
Code Review

Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the coding blocks). Grading wise, we are looking for that you understand your code and what you did.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import ObjectProperty

from kivy.vector import Vector
from kivy.clock import Clock
"""installs necessary widgets from kivy library."""

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

<Ball>:
    size: 50, 50 
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size          

<Bat>:
    size: 25, 200
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size

<Game>:
    ball: pong_ball
    first_player: player_left
    second_player: player_right
    
    canvas:
        Rectangle:
            pos: self.center_x - 5, 0
            size: 10, self.height
    
    Label:
        font_size: 70  
        center_x: root.width / 4
        top: root.top - 50
        text: str(root.first_player.score)
        
    Label:
        font_size: 70  
        center_x: root.width * 3 / 4
        top: root.top - 50
        text: str(root.second_player.score)
    
    Ball:
        id: pong_ball
        center: self.parent.center
        
    Bat:
        id: player_left
        x: root.x
        center_y: root.center_y
        
    Bat:
        id: player_right
        x: root.width - self.width
        center_y: root.center_y
The YML is saying how the screen is going to look. How many pixels the the ball, bat and screen are. 
Major Challenges

Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.
It was an extremely challenging project but I learned many things about how to make applications run and how to organize code. Overall learning about how to inherit in classes was extremely useful. 
Example Runs

Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

Testing

How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission.
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
    I used unittest to ensure each piece of the program was working correctly. 
Make it easy for us to know you ran the project and tested the project before you submitted this report!
Missing Features / What's Next

Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future.
I would have liked to create goal point score so there is a winner in the game. Also, I would have liked to make a menu screen with difficulty levels with different speeds. Lastly, I would have liked to make an AI that moved player 2. 
Final Reflection

Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
The course was extremely challenging being my first ever experience learning code. It was very intensive and pushed a massive amount of information into my head. I am confident to say that I am able to walk away knowing so much more about coding than I did before I took the course. Even though I struggled my way through the course, I am miles ahead of wehre I started and I feel extremely proud. 
