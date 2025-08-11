from classes.graph import Graph

from utils.wl import wl


def isomorph(u: Graph, v: Graph) -> int:
    if u.order() != v.order() or u.size() != v.size():
        return 0

    cu = wl(u)
    cv = wl(v)

    if cu.colors_historgram != cv.colors_historgram:
        return 0

    return 1
