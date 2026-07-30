import random


def rand_grid(box, nb: int = 100):
    start_col, start_row, end_col, end_row = box
    data = set()
    for _ in range(nb):
        data.add(
            (random.randrange(
                start_row, end_row), random.randrange(
                start_col, end_col)))
    print(data)
    return data

# Generate figures at defined location


def gen_blinker(col: int, row: int):
    return {(col, row), (col, row + 1), (col, row + 2)}


def gen_vaissel(col: int, row: int):
    return {(col, row), (col, row + 1), (col, row + 2),
            (col + 1, row + 2), (col + 2, row + 1)}


def gen_beacon(col: int, row: int):
    return {(col, row), (col, row + 1), (col + 1, row),
            (col + 3, row + 2), (col + 3, row + 3), (col + 2, row + 3)}


def gen_toad(col: int, row: int):
    return {(2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)}

# DATA

# x,y


# Toad
# active_cells = {(2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)}
