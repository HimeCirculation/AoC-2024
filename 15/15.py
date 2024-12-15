class Vector:
    def __init__(self, data):
        self.data = list(data)
        self.dimension = len(data)

    def __add__(self, other: "Vector"):
        if isinstance(other, int) or isinstance(other, float):
            return Vector([a + other for a in self.data])

        if self.dimension != other.dimension:
            raise ValueError

        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __mul__(self, other):
        if not isinstance(other, int):
            raise ValueError

        return Vector([a * other for a in self.data])

    def __mod__(self, other):
        if isinstance(other, int):
            other = Vector([other] * self.dimension)

        if other.dimension != self.dimension:
            raise ValueError("None conformable Vector objects")

        return Vector([a % b for a,b in zip(self, other)])

    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index >= self.dimension:
            raise StopIteration

        output = self[self.index]
        self.index += 1
        return output

    def __getitem__(self, item):
        return self.data[item]

    def __eq__(self, other):
        if self.dimension != other.dimension:
            return False
        for a,b in zip(self.data, other.data):
            if a != b:
                return False
        return True

    def __str__(self):
        return str(self.data).replace("[", "<").replace("]", ">")


def parse(fp):
    with open(fp, "r") as file:
        grid, moves = file.read().split("\n\n")
    grid = [list(line) for line in grid.split("\n")]
    moves = moves.replace("\n", "")

    return grid, moves

directions = {"^": Vector([-1, 0]),
              ">": Vector([0, 1]),
              "v": Vector([1, 0]),
              "<": Vector([0, -1])}

def find_robot(grid: list[list[str]]):
    for i, line in enumerate(grid):
        if line.index("@") != -1:
            return i, line.index("@")
    raise ValueError("Couldnt find robot in grid")


