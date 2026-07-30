"""

Grid:

    - infinite grid
    - we only handle active cells

Cell:

    - cell are represented has `tuple[int, int] (row, col) ou col row ?

Règle:

    L'état suivant d'une cellule est actif si elle a 3 voisins actifs ou elle est active et a 2 voisins actifs

"""

import collections

ALIVE = "◼"
DEAD = "."

# Above left, Above, Above right, Left, Right, Below left, Below, Below right
NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1))


class LifeGrid:

    def __init__(
            self, active_cells: set[tuple[int, int]], bbox=(0, 0, 30, 30)):
        self.active_cells = active_cells
        self.bbox = bbox

    def evolve(self):

        num_neighbors = self.count_neighbors()

        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.active_cells

        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.active_cells

        self.active_cells = stay_alive | come_alive

    def evolve_explicit(self):
        # 1. On compte le nombre de voisins pour chaque cellule
        num_neighbors = self.count_neighbors()

        # 2. On initialise le futur prochain set
        cells = set()

        # 3. On parcourt chaque cellule et son nombre de voisins
        for cell, num in num_neighbors.items():
            # Si la cellule a 2 ou 3 voisins ET qu'elle est déjà active, elle reste en vie
            # ou Si la cellule a exactement 3 voisins ET qu'elle n'est pas
            # active, elle naît
            if (num in [2, 3] and cell in self.active_cells) or (
                    num == 3 and cell not in self.active_cells):
                cells.add(cell)

        # 4. On set la nouvelle géération de cellules
        self.active_cells = cells

    # eval number of neighbors far all active cells
    # return a collections indexed by tuple (row, col)
    def count_neighbors(self):
        num_neighbors = collections.defaultdict(int)
        for row, col in self.active_cells:
            for drow, dcol in NEIGHBORS:
                num_neighbors[(row + drow, col + dcol)] += 1
        return num_neighbors

    def as_string(self, gen: int, total: int):
        start_col, start_row, end_col, end_row = self.bbox

        title = f"Game of life: {gen}/{total} - box: {self.bbox}"

        display = [title.center(2 * (end_col - start_col))]

        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row, col) in self.active_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        return "\n ".join(display)
