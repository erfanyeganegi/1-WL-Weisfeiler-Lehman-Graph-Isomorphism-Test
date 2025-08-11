from classes.graph import Graph
from classes.coloring import Coloring
from classes.signature import Signature


def signature(g: Graph, c: Coloring, u: int) -> Signature:
    adjacent_colors = []
    for _, v in g.edges_from(u):
        adjacent_colors.append(c.get_color(v))
    adjacent_colors.sort()

    return Signature(c.get_color(u), adjacent_colors)
