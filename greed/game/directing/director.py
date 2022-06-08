import random as r
from game.casting.stone import Stone
from game.shared.point import Point
from game.shared.color import Color

# from game.casting.cast import Cast

WHITE = Color(255, 255, 255)
GREEN = Color(0, 255, 0)
RED = Color(255, 0, 0)

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        # get direction to move from keyboard service
        user = cast.get_first_actor("user")
        velocity = self._keyboard_service.get_direction()
        user.set_velocity(velocity)  
        # user.set_velocity(Point(-15, 0))      
        # user actor = direction horizontal only

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        # create rocks, gems at top of screen (random x, set y)(random number of stones)

        # random color range
        r_main = r.randint(160, 225)
        r_sub1 = r.randint(1,150)
        r_sub2 = r.randint(1,150)

        gem = Stone()
        gem.set_text("*")
        gem.set_points(1)
        gem.set_velocity(Point(0,5))
        gem.set_position(Point(r.randint(15, 885),15))
        green = Color(r_sub1, r_main, r_sub2)
        gem.set_color(green)

        rock = Stone()
        rock.set_text("o")
        rock.set_points(-1)
        rock.set_velocity(Point(0,5))
        rock.set_position(Point(r.randint(15, 885),15))
        blue = Color(r_sub1,r_sub2,r_main)
        rock.set_color(blue)

        cast.add_actor("stones", gem)
        cast.add_actor("stones", rock)

        # move player, rocks, gems
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        # loop to move all actors
        user = cast.get_first_actor("user")
        user_x = user.get_position().get_x()
        user_y = user.get_position().get_y()
        score = cast.get_first_actor("score")
        for actor in cast.get_actors("stones"):
            actor.move_next(max_x, max_y)
            # check for collisions
            if actor.get_text() == "*":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()
                if ((user_x - 10 < actor_x < user_x + 10) and (user_y - 10 < actor_y < user_y + 10)):
                    score.add_points(1)
                if actor_y > max_y - 30 or((user_x - 10 < actor_x < user_x + 10) and (user_y - 10 < actor_y < user_y + 10)):
                    cast.remove_actor("stones", actor)
                    
            elif actor.get_text() == "o":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()
                if ((user_x - 10 < actor_x < user_x + 10) and (user_y - 10 < actor_y <user_y + 10)):
                    score.add_points(-1)
                if actor_y > max_y - 30 or ((user_x - 10 < actor_x < user_x + 10) and (user_y - 10 < actor_y < user_y + 10)):
                    cast.remove_actor("stones", actor)

        # move player
        user.move_next(max_x, max_y)

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        # stones = cast.get_actors("stones")
        user = cast.get_first_actor("user")
        score = cast.get_first_actor("score")
        score.set_text(f"SCORE: {score.get_points()}")
        # Set score color: green if 0 and above; red if negative
        if score.get_points() >= 0:
            score.set_color(GREEN)
        else:
            score.set_color(RED)

        # Set score milestones text:
        if score.get_points() >= 5 and score.get_points() <=10:
            score.set_text(f"SCORE: {score.get_points()} : You're on a roll!")
        elif score.get_points() >= 11 and score.get_points() <=15:
            score.set_text(f"SCORE: {score.get_points()} : Can you reach 30?")
        elif score.get_points() >= 31 and score.get_points() <=40:
            score.set_text(f"SCORE: {score.get_points()} : Amazing reflexes!")
        elif score.get_points() >= 48 and score.get_points() <=50:
            score.set_text(f"SCORE: {score.get_points()} : Nothing's stopping you now!")
        elif score.get_points() <= -5 and score.get_points() <= -8:
            score.set_text(f"SCORE: {score.get_points()} : Pick up the pace.")

        for actor in cast.get_actors("stones"):
            self._video_service.draw_actor(actor)
        self._video_service.draw_actor(user)
        self._video_service.draw_actor(score)
        self._video_service.flush_buffer()
