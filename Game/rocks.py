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
        """Updates the appearance of the rock.
        
        Args:
            rock: The given appearance of the rock.
        """
        self._rock = rock

    def get_rock_position(self):
        """Gets the rock's current coordinates.
        
        Returns:
            The rock's current coordinates.
        """
        self._position.x = float(random.uniform(-600, 600))
        self._position.y = 600

    def get_rock_velocity(self):
        """Gets the rock's current speed and direction.
        
        Returns:
            The rock's current speed and direction.
        """
        return self._velocity

    def set_rock_position(self, position):
        """Updates the coordinates of the rock.
        
        Args:
            position: The given coordinates of the rock.
        """
        self._position = position

    def set_rock_velocity(self, velocity):
        """Updates the speed and direction of the rock.
        
        Args:
            velocity: The given speed and direction of the rock.
        """
        self._velocity = velocity

    def hit(self):
        """
        Sets rock to false when hit by player and adds a score

        Returns:
            The points scored
        """
        self.alive = False
        self.score = -1
        return self.score
