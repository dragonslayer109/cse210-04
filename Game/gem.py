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
        self.score = 0
        self.alive = True
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
            gem: The given appearance of the gem.
        """
        self._gem = gem
    
    def get_gem_position(self):
        """Gets the gem's current coordinates.
        
        Returns:
            The gem's current coordinates.
        """
        self._position.x = float(random.uniform(-600, 600))
        self._position.y = 600

    def get_gem_velocity(self):
        """Gets the gem's current speed and direction.
        
        Returns:
            The gem's current speed and direction.
        """
        return self._velocity

    def set_gem_position(self, position):
        """Updates the coordinates of the gem.
        
        Args:
            position: The given coordinates of the gem.
        """
        self._position = position

    def set_gem_velocity(self, velocity):
        """Updates the speed and direction of the gem.
        
        Args:
            velocity: The given speed and direction of the gem.
        """
        self._velocity = velocity

    def hit(self):
        """
        Sets gem to false when hit by player and adds a score

        Returns:
            The points scored
        """
        self.alive = False
        self.score = 1
        return self.score
