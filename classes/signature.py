class Signature:
    def __init__(self, color: str, adjacent_colors: list[str]):
        self.color = color
        self.adjacent_colors = adjacent_colors

    def __str__(self) -> str:
        return f"{self.color}, {self.adjacent_colors}"
