from classes.graph import Graph

from utils.wl import wl


def isomorph(u: Graph, v: Graph) -> int:
    if u.order() != v.order() or u.size() != v.size():
        return 0

    cu, histc = wl(u)
    cv, histv = wl(v)

    if len(histc != histv:
        return 0

    return 1
