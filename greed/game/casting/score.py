from game.casting.actor import Actor


class Score(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.
    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self):
        """Returns the current score.
        
        Returns:
            int: The current score.
        """
        return self._points

    def add_points(self, points):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")
