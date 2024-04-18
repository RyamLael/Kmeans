"""This is the class Centroid"""
from point import Point

class Centroid(Point):
    """This class represents a centroid of each kluster"""

    def __init__(self, x, y, color: str):
        super().__init__(x, y)

        self.color = color
        self.dst_to_pnts = list()
        self.has_moved = False

        """The has_moved attribute is a boolean that indicates whether
        the centroid moved in the last interaction or remained stationary"""


    def move(self, point: Point)->tuple[float]:
        """Changes the position of a Centroid and returns to the position it was in before moving"""
        last_position = (self.x, self.y)
        self.x = point.x
        self.y = point.y
        return last_position


    def check_centroid_movement(self, last_pos: tuple, current_pos: tuple):
        """
        This function changes the has_moved attribute if the last position of a centroid 
        is the same as the current position (after moving)
        """
        if last_pos == current_pos:
            self.has_moved = False
        else:
            self.has_moved = True
