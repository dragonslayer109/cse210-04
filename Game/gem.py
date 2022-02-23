import random
from point import Point
from actor import Actor

class Gem(Actor):
    """
    The visual representation of the Gem in the game. 
    This class keeps track of the appearance, position and velocity of the Gem.

    Inherits 
    """
    def __init__(self):
        super().__init__()
        self._gem = "*"
     
    def get_gem(self):
        """Gets the gem's visual appearance.
        
        Returns:
            The gem's visual appearance.
        """
        return self._gem
    
    def set_gem(self, gem):
        """Updates the appearance of the gem.
        
        Args:
            gem: The given appearance of the Actor.
        """
        self._gem = gem
