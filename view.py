import curses
from time import sleep
from grid import LifeGrid

class CursesView:
    """
    RENDER 
        - render grid using curses

    """
        
    def __init__(self, grid: LifeGrid, max=40, frame_rate=6):
        self.grid = grid
        self.max = max
        self.frame_rate = frame_rate

    def show(self):
        curses.wrapper(self._draw)

    def _draw(self, screen):
        
        curses.curs_set(0)
        screen.clear()

        # May fail if terminal is too small
        screen.addstr(0, 0, self.grid.as_string(0, self.max))
        screen.refresh()
        
        # Pause to see the start pos
        sleep(1)

        for i in range(self.max):
            self.grid.evolve()

            screen.addstr(0, 0, self.grid.as_string(i, self.max))
            screen.refresh()
            sleep(1 / self.frame_rate)