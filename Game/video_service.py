import pyray

class VideoService:
    """This class renders the various elements of the game onto the screen. 
    """

    def __init__(self, width, height, cell_size, frame_rate):
        """Constructs a new VideoService.
        """
        self._width = width
        self._height = height
        self._cell = cell_size
        self._frame_rate = frame_rate

    def is_window_open(self):
        """Checks to see if the window was closed by the player.

        Returns:
            Value of "True" if the window is closed. Value of "False" if the window is still open.
        """
        return not pyray.window_should_close()

    def get_cell(self):
        """Gets the screen's cell size.
        
        Returns:
            The screen's cell size.
        """
        return self._cell

    def get_height(self):
        """Gets the screen's height.
        
        Returns:
            The screen's height.
        """
        return self._height

    def get_width(self):
        """Gets the screen's width.
        
        Returns:
            The screen's width.
        """
        return self._width

    def open_window(self):
        """Opens a new window.
        """
        pyray.init_window(self._width, self._height)
        pyray.set_target_fps(self._frame_rate)

    def grid(self):
        """Draws a grid on the screen."""
        for y in range(0, self._height, self._cell):
            pyray.draw_line(0, y, self._width, y, pyray.WHITE)
        for x in range(0, self._width, self._cell):
            pyray.draw_line(x, 0, x, self._height, pyray.WHITE)

    def start_drawing(self):
        """Starts drawing the elements on the screen.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        self.grid()

    def draw_actor(self, actor):
        """Draw the Actor on the screen.

        Args:
            actor: The visual representation of the player in the game.
        """ 
        player = actor.get_player()
        x = actor.get_player_position().get_x()
        y = actor.get_player_position().get_y()
        pyray.draw_text(player, x, y)
    
    def end_drawing(self):
        """Ends the drawing.
        """ 
        pyray.end_drawing()

    def close_window(self):
        """Closes the window."""
        pyray.close_window()