from game.casting.actor import Actor


class Stone(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.
    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def set_points(self, points):
        self.points = points
    
    def get_points(self):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        return self._points
