from classes.graph import Graph
from classes.coloring import Coloring

from utils.signature import signature


def wl(g: Graph) -> Coloring:
    c = Coloring()

    while True:
        signatures = {}
        old_partition = c.partition()

        for u in g.nodes:
            signatures[u] = signature(g, c, u)

        for u in g.nodes:
            c.set_color(u, signatures[u])

        if c.partition() == old_partition:
            break

    return c
