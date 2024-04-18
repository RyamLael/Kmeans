"""this is the kmeans class which is responsible for applying the kmeans algorithm"""
from centroid import Centroid
from plan import Plan

class KmeansAlgorithm:
    """This class represents how kmeans works performing its entire algorithm throughout the code"""

    def __init__(self, plan: Plan):
        self.plan = plan

    def algorithm(self):
        """
        The algotithm must follow the following steps:
        1.Calculate the distance between the centroids and the points
        2.Classify each point with it respective centroid
        3.move the centroid to the average of each point belonging to it
        4.Repeat the process until the centroids show no change 
        """
        while True:
            self.calc_cntrd_distance()
            self.classificate_pnts(self.plan.centroids[0], self.plan.centroids[1])
            self.move_centroids()

            if self.no_cntr_moved():
                break
            for centroid in self.plan.centroids:
                centroid.has_moved = False


    #Step 1, Calculate the distance between the centroids and the points
    def calc_cntrd_distance(self):
        """
        This function calculates the distance between the centroid and each point on a plane and 
        changes the dst_to_pnts attribute of each centroid with a point and a distance to it
        """
        for centroid in self.plan.centroids:
            centroid.dst_to_pnts = []
            for point in self.plan.points:
                distance = self.plan.distance_btwn_points(centroid, point)
                centroid.dst_to_pnts.append((point, distance))


    #Step 2, Classify each point with it respective centroid
    def classificate_pnts(self, centroid1: Centroid, centroid2: Centroid):
        """This function changes the color of plan points to the color of the closer centroid"""

        for point1, point2 in (zip(centroid1.dst_to_pnts, centroid2.dst_to_pnts)):
            #the dst_to_pnts list stores tuples in which the first element is the point
            #and the second element is the distance to that point

            dst_ctrd1 = point1[1]
            dst_ctrd2 = point2[1]

            if dst_ctrd1<dst_ctrd2:
                point1[0].color = centroid1.color
            else:
                point2[0].color = centroid2.color


    #Step 3, move the centroid to the average of each point belonging to it
    def move_centroids(self):
        """moves the centroids to the middle of the points that belong to it"""

        #interate each centroid of a plan
        for centroid in self.plan.centroids:
            cntrd_pnts = []

            for point in self.plan.points:
                if point.color == centroid.color:
                    cntrd_pnts.append(point)
            #move o ponto e retorna a posição dele antes de se mover
            last_pos = centroid.move(self.plan.midpnt_of_pnts(cntrd_pnts))
            centroid.check_centroid_movement(last_pos, (centroid.x, centroid.y))


    def no_cntr_moved(self)->bool:
        """Returns true if no centroid have move or false if some centroid moved"""
        for centroid in self.plan.centroids:
            if centroid.has_moved:
                return False
        return True
