from hashlib import sha256
from collections import defaultdict

from classes.signature import Signature


class Coloring:
    def __init__(self, default=sha256("0, []".encode()).hexdigest()):
        self.colors: defaultdict[int, str] = defaultdict(lambda: default)
        self.colors_historgram: defaultdict[str, int] = defaultdict(int)

    def get_color(self, u: int) -> str:
        return self.colors[u]

    def set_color(self, u: int, signature: Signature):
        self.colors[u] = sha256(str(signature).encode()).hexdigest()
        self._update_histogram(self.colors[u])

    def partition(self):
        partitions = defaultdict(set)
        for u, c in self.colors.items():
            partitions[c].add(u)
        return {frozenset(group) for group in partitions.values()}

    def _update_histogram(self, c: str):
        self.colors_historgram[c] += 1
