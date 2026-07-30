from grid import LifeGrid
from view import CursesView
from utils import rand_grid, gen_blinker, gen_vaissel, gen_beacon, gen_toad


# DATA

# big screen
# box = (0, 0, 100, 60)
# seedbox = (35, 15, 65, 45)

# smaller screen
box = (0, 0, 90, 50)
seedbox = (15, 15, 75, 35)

# Specific data
# active_cells = rand_grid(seedbox, 300)

# active_cells = set()

# active_cells = gen_blinker(25, 45)

# active_cells = active_cells.union(gen_vaissel(25, 45))
# active_cells = active_cells.union(gen_vaissel(20, 45))
# active_cells = active_cells.union(gen_vaissel(25, 50))
# active_cells = active_cells.union(gen_vaissel(20, 50))

# active_cells = active_cells.union(gen_beacon(25, 45))

# active_cells = active_cells.union(gen_toad(25, 45))

# Rand data
active_cells = rand_grid(seedbox, 300)


# RUN

grid = LifeGrid(active_cells, box)

view = CursesView(grid, 500, 6)
view.show()
