import random
from grid import LifeGrid
from view import CursesView 

def randGrid(box, nb: int = 100):
    start_col, start_row, end_col, end_row = box
    data = set()
    for _ in range(nb):
        data.add((random.randrange(start_row, end_row), random.randrange(start_col, end_col)))
    print(data)
    return data


# DATA

# x,y

# Blinker
#active_cells = {(2, 1), (2, 2), (2, 3), (3, 2)}

# Toad
#active_cells = {(2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)}

# Beacon
#active_cells = {(1, 1), (1, 2), (2, 1), (4, 3), (4, 4), (3, 4)}

# Truc
#active_cells = {(12, 11), (12, 12), (12, 13), (13, 12)}

# 3 trucs
# active_cells = {
#     (12, 11), (12, 12), (12, 13), (13, 12),
#     (17, 16), (17, 17), (17, 18), (18, 17),
#     (22, 21), (22, 22), (22, 23), (23, 22),
# }


# mover
#active_cells = {(2, 1), (2, 2), (2, 3), (1, 3), (0, 2)}

# DATA

rows = 100
cols = 60
box = (0, 0, rows, cols)

seedbox = (35, 15, 65, 45)
active_cells = randGrid(seedbox, 160)


# RUN

grid = LifeGrid(active_cells, box)

view = CursesView(grid, 1000, 6)
view.show()



