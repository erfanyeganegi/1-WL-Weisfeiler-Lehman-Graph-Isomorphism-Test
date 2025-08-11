from typing import List, Tuple


class Graph:
    def __init__(self):
        self.nodes: List[int] = []
        self.edges: List[Tuple[int, int]] = []

    def add_node(self, *nodes: int):
        self.nodes.extend(nodes)

    def add_edge(self, *edges: Tuple[int, int]):
        self.edges.extend(edges)

    def edges_from(self, v: int) -> List[Tuple[int, int]]:
        return [edges for edges in self.edges if edges[0] == v]

    def order(self):
        return len(self.nodes)

    def size(self):
        return len(self.edges)
