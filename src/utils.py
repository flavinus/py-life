import random
from grid import Bounds, Cells

# Generates random grid
def rand_grid(bounds: Bounds, nb: int = 100):
    min_x, min_y, max_x, max_y = bounds
    data = set()
    for _ in range(nb):
        data.add((random.randrange(min_x, max_x), random.randrange(min_y, max_y)))
    return data

# Transformations

def translate(cells: Cells, cols: int, rows: int):
    output = set()
    for col, row in cells:
        output.add((row + rows, col + cols))
    return output

def rotate(cells: Cells) -> Cells:
    xs = [x for x, y in cells]
    ys = [y for x, y in cells]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # Centre de la figure
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    output = set()
    for (x, y) in cells:
        # Translation pour centrer sur (0,0)
        x_rel = x - center_x
        y_rel = y - center_y

        # Rotation 90° horaire : (x, y) -> (y, -x)
        new_x_rel = y_rel
        new_y_rel = -x_rel

        # Translation inverse pour replacer le centre
        new_x = new_x_rel + center_x
        new_y = new_y_rel + center_y

        # On arrondit car les coordonnées doivent être entières
        output.add((round(new_x), round(new_y)))

    return output

# todo: flip ?
