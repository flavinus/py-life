import curses
from time import sleep
from _curses import window
from view.abstract import ViewInterface
from grid import LifeGrid


ALIVE = "◼"
DEAD = " "

class CursesView(ViewInterface):
    """
    RENDER
        - render grid using curses
    """

    def __init__(self, frame_rate: int = 5):
        self.frame_rate = frame_rate
        self.stdscr = curses.initscr()
        self.rows = round((curses.COLS - 1) / 2)
        self.cols = curses.LINES - 1
        self.grid = None
        self.screen = None

    def start(self, grid: LifeGrid):
        self.grid = grid
        curses.curs_set(0)
        curses.wrapper(self.exec)

    def exec(self, screen: window):
        self.screen = screen
        while True:
            self.draw()
            sleep(1 / self.frame_rate)

            if self.grid.evolve() == 0:
                print("ERROR: No more alive cells !!! 😵")
                break

    def draw(self):

        title = f"[ Game of life ] Iteration={self.grid.iteration} Cells={len(self.grid.cells)} Bounds={self.rows}x{self.cols}"
        display = [title]

        for row in range(0, self.cols):
            display_row = [
                ALIVE if (row, col) in self.grid.cells else DEAD
                for col in range(0, self.rows)
            ]
            display.append(" ".join(display_row))

        output = "\n ".join(display)

        self.screen.addstr(0, 0, output)
        self.screen.refresh()

    def get_bounds(self):
        return (0, 0, self.cols, self.rows)
