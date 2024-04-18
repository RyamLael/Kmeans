"""This is the class that will make a graph"""
import matplotlib.pyplot as plt

from kmeans_algorithm import KmeansAlgorithm
# from plan import Plan


class Graph:
    """
    this class interacts with the kmeans algorithm and visually shows what is happening
    """

    def __init__(self, kmeans: KmeansAlgorithm):

        self.kmeans = kmeans

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)

        self.fig.suptitle('K-means')

        self.kmeans.algorithm()
        self.set_up(self.ax)

        plt.show()

    # para fazer a animação, preciso plotar cada mudança de estado do plano

    def set_up(self, ax) -> None:
        """Plot points and centroids on the graph"""
        centroid_axes = self.set_centroids_axes()
        point_axes = self.set_points_axes()

        self.plot_centroid_axes(centroid_axes, ax)
        self.plot_point_axes(point_axes, ax)

        plt.xlim(0, 100)
        plt.ylim(0, 100)

    def set_points_axes(self):
        """Create 3 lists: x-coordinates, y-coordinates and colors 
        then Return a tuple containing these three lists"""

        pnt_x = []
        pnt_y = []
        pnt_color = []

        for p in self.kmeans.plan.points:
            pnt_x.append(p.x)
            pnt_y.append(p.y)
            pnt_color.append(p.color)
        point_axes = (pnt_x, pnt_y, pnt_color)
        return point_axes

    def set_centroids_axes(self) -> tuple:
        """Create 3 lists: x-coordinates, y-coordinates and colors 
        then Return a tuple containing these three lists"""

        cntrd_x = []
        cntrd_y = []
        cntrd_color = []
        for p in self.kmeans.plan.centroids:
            cntrd_x.append(p.x)
            cntrd_y.append(p.y)
            cntrd_color.append(p.color)
        centroid_axes = (cntrd_x, cntrd_y, cntrd_color)
        return centroid_axes

    def plot_centroid_axes(self, centroid_axes: tuple, ax):
        """Plots the centroid in the parameter axes"""
        ax.scatter(centroid_axes[0], centroid_axes[1], label='Centroids',
                   c=centroid_axes[2], edgecolor='k', marker='o', s=150)

    def plot_point_axes(self, point_axes: tuple, ax):
        """Plots the points in the parameter axes"""
        ax.scatter(point_axes[0], point_axes[1],
                   label='Points', c=point_axes[2])
