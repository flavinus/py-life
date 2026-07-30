import collections

type Cell = tuple[int, int]
type Cells = set[Cell]
type Bounds = tuple[int, int, int, int]

# Above left, Above, Above right, Left, Right, Below left, Below, Below right
NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

class LifeGrid:

    def __init__(self, cells: Cells):
        self.cells = cells
        self.iteration = 0

    def evolve(self):
        # On compte le nombre de voisins pour chaque cellule
        num_neighbors = self._count_neighbors()

        # On parcourt chaque cellule et son nombre de voisins
        cells = set()
        for cell, num in num_neighbors.items():
            # Si la cellule a 2 ou 3 voisins ET qu'elle est déjà active, elle reste en vie
            # ou Si la cellule a exactement 3 voisins ET qu'elle n'est pas
            # active, elle naît
            if (num in [2, 3] and cell in self.cells) or (
                    num == 3 and cell not in self.cells):
                cells.add(cell)

        # On set la nouvelle géération de cellules
        self.cells = cells
        self.iteration += 1

        return len(self.cells)

    # eval number of neighbors for each active cell
    # returns a collections indexed by tuple (row, col)
    def _count_neighbors(self):
        num_neighbors = collections.defaultdict(int)
        for row, col in self.cells:
            for drow, dcol in NEIGHBORS:
                num_neighbors[(row + drow, col + dcol)] += 1
        return num_neighbors
