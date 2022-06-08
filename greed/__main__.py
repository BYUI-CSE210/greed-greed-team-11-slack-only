import os
import random

from game.casting.actor import Actor
from game.casting.stone import Stone
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 30
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
GREEN = Color(0, 255, 0)
RED = Color(255, 0, 0)
YELLOW = Color(139,139,0)

def main():
    
    # create the cast
    cast = Cast()
    # create the robot
    x = int(MAX_X / 2)
    y = int(570)
    position = Point(x, y) 
    #create the player
    user = Actor()
    user.set_text("@")
    user.set_font_size(FONT_SIZE)
    user.set_color(YELLOW)
    user.set_position(position)
    cast.add_actor("user", user)
    # create initial score
    score = Score()
    score.set_position(Point(MAX_X // 3, 15))
    score.set_color(GREEN)
    cast.add_actor("score", score)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()
