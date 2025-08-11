from classes.graph import Graph
import yaml

from utils.isomoprh import isomorph


def load_graph(path):
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    g = Graph()
    g.add_node(*data["graph"]["vertices"])
    g.add_edge(*data["graph"]["edges"])

    return g


if __name__ == "__main__":
    U = load_graph("graphs/Tree(A).yaml")
    V = load_graph("graphs/Tree(B).yaml")

    print(isomorph(U, V))
