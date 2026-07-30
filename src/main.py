from grid import LifeGrid
from view.curse import CursesView
from view.graphic import GraphicView
from utils import *
from patterns import get_pattern

# VIEW: Init view first to know the number of available cols and rows
#view = CursesView()
view = GraphicView()

# RAND SEED: generated inside view bounds and number of cells depends on bounds
bounds = view.get_bounds()
count = round((bounds[2] * bounds[3]) / 7)
cells = rand_grid(bounds, count)

# RUN
view.start(LifeGrid(cells))
