import random
from point import Point
from actor import Actor

class Rock(Actor):
    """
    The visual representation of the rocks in the game. 
    This class keeps track of the appearance, position and velocity of the Rock.

    Inherits 
    """
    def __init__(self):
        super().__init__()
        self._rock = "o"

    def get_rock(self):
        """Gets the Rock's visual appearance.
        
        Returns:
            The Rock's visual appearance.
        """
        return self._rock
    
    def set_rock(self, rock):
        """Updates the appearance of the Actor.
        
        Args:
            rock: The given appearance of the Actor.
        """
        self._rock = rock