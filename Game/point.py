class Point:
    """This class calculates the current position of a given object on the screen
    using x and y coordinates.

    Attr:
        _x: The x (horizontal) coordinates.
        _y: The y (vertical) coordinates.
    """
    
    def __init__(self, x, y):
        """Constructs a new Point according to the given x and y coordinates.
        
        Args:
            x: The x (horizontal) coordinates.
            y: The y (vertical) coordinates.
        """
        self._x = x
        self._y = y

    def get_x(self):
        """Gets the x (horizontal) coordinates.
        
        Returns:
            The x (horizontal) coordinates.
        """

        return self._x

    def get_y(self):
        """Gets the y (vertical) coordinates.
        
        Returns:
            The y (vertical) coordinates.
        """

        return self._y

    def equal(self, new):
        """Checks whether the new coordinates and old coordinates are equal meaning
        that the object on the screen hasn't moved.

        Args:
            new: The new coordinates of the object.

        Returns: 
            A Value of "True" if the x and y coordinates are equal and a Value of "False"
            if the x and y coordinates are not equal.
        """

        return self._x == new.get_x() and self._y == new.get_y()

    def scale(self, scale_value):
        """
        Scales the object by the given value.

        Args:
            scale_value: The amount to scale by.
            
        Returns:
            A new Point that is scaled.
        """
        return Point(self._x * scale_value, self._y * scale_value)

    def sum(self, new):
        """Constructs a new Point from the sum of the new one and the old one.

        Args:
            new: The new coordinates for the new Point.

        Returns:
            A new Point that is the sum of the old one and new one.
        """
        x = self._x + new.get_x()
        y = self._y + new.get_y()
        
        return Point(x, y)