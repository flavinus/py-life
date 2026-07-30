import pygame
from grid import LifeGrid
from view.abstract import ViewInterface

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1000
CELL_SIZE = 8

class GraphicView(ViewInterface):

    def __init__(self, frame_rate: int = 15):
        self.grid = None
        self.running = False
        self.frame_rate = frame_rate

        pygame.init()
        pygame.display.set_caption('Game of life')
        pygame.display.set_icon(pygame.image.load("assets/flavinus_400.png"))
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()


    def start(self, grid: LifeGrid):
        self.grid = grid
        self.running = True

        while True:
            #print(f"[ Game of life ] Iteration={self.grid.iteration} Cells={len(self.grid.cells)}")
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.running = not self.running
            elif keys[pygame.K_ESCAPE]:
                break

            if self.running and self.grid.evolve() == 0:
                print("ERROR: No more alive cells !!! 😵")
                break

            self.clock.tick(self.frame_rate)

        pygame.quit()
        #sys.exit()


    def draw(self):
        self.screen.fill(BLACK)
        for y in range(0, WINDOW_WIDTH):
            for x in range(0, WINDOW_HEIGHT):
                if (x, y) in self.grid.cells:
                    pygame.draw.rect(self.screen, WHITE, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()

    def get_bounds(self):
        return (0, 0, round(WINDOW_WIDTH / CELL_SIZE), round(WINDOW_HEIGHT / CELL_SIZE))
