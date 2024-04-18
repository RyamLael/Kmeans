"""Main of project"""

from graph import Graph
from kmeans_algorithm import KmeansAlgorithm
from plan import Plan

cores_centroides = ['r', 'b']
plano = Plan(100, cores_centroides)

graph = Graph(KmeansAlgorithm(plano))
