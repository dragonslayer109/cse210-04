from Game import Point


class Actor:
    """The visual representation of the player in the game. 
    This class keeps track of the appearance, position and velocity of the Actor.

    Attr:
        _player: The visual appearance of the player.
        _position: The coordinates of the player on the screen.
        _velocity: The speed and direction of the player.
    """

    def __init__(self):
        """Constructs the Actor."""
        self._player = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_player(self):
        """Gets the Actor's visual appearance.
        
        Returns:
            The Actor's visual appearance.
        """
        return self._player

    def get_player_position(self):
        """Gets the Actor's current coordinates.
        
        Returns:
            The Actor's current coordinates.
        """
        return self._position

    def get_player_velocity(self):
        """Gets the Actor's current speed and direction.
        
        Returns:
            The Actor's current speed and direction.
        """
        return self._velocity
    
    def next_move(self, max_x, max_y):
        """Moves the Actor to its next position.
        
        Args:
            max_x: The maximum x coordinates.
            max_y: The maximum y coordinates.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def set_player(self, player):
        """Updates the appearance of the Actor.
        
        Args:
            player: The given appearance of the Actor.
        """
        self._player = player

    def set_player_position(self, position):
        """Updates the coordinates of the Actor.
        
        Args:
            position: The given coordinates of the Actor.
        """
        self._position = position

    def set_player_velocity(self, velocity):
        """Updates the speed and direction of the Actor.
        
        Args:
            velocity: The given speed and direction of the Actor.
        """
        self._velocity = velocity