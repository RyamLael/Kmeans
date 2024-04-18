"""This is the class Plan that be used to receive the poits and the centroids"""
import random

from point import Point
from centroid import Centroid


class Plan:
    """This class represents a plan with points and centroids"""

    def __init__(self, qnt_pnts: int, cntrds_colors: list[str]):
        self.points = self.set_up_points(qnt_pnts)
        self.centroids = self.set_up_centroids(cntrds_colors)

    def set_up_points(self, qunt_pnts: int) -> list:
        """Returns a list of points to set up points in plan"""
        point_list = []
        for _ in range(qunt_pnts):
            px = random.uniform(0, 100)
            py = random.uniform(0, 100)
            point_list.append(Point(px, py))
        return point_list

    def set_up_centroids(self, colors: "str"):
        """Returns a list of centroids to set up centroids in plan"""
        centroid_list = []
        for color in colors:
            cx = random.uniform(0, 100)
            cy = random.uniform(0, 100)
            centroid_list.append(Centroid(cx, cy, color))
        return centroid_list

    def distance_btwn_points(self, start: Centroid, end: Point) -> float:
        """This method calculates a distance between two points"""
        distance = ((end.x-start.x)**2+(end.y-start.y)**2)**(1/2)
        return distance

    def midpnt_of_pnts(self, pointlist: list[Point]):
        """This function returns a point that is in the middle of the parameter points"""
        sum_x = 0
        sum_y = 0

        for point in pointlist:
            sum_x += point.x
            sum_y += point.y

        medium_point = Point(sum_x/len(pointlist), sum_y/len(pointlist))
        return medium_point
