import pygame
from grid import LifeGrid
from view.abstract import ViewInterface

BG_COLOR = (0, 0, 0)
CELL_COLOR = (200, 200, 200)
CELL_SIZE = 5

class GraphicView(ViewInterface):

    def __init__(self, frame_rate: int = 10):
        pygame.init()
        pygame.display.set_caption('Game of life')
        pygame.display.set_icon(pygame.image.load("assets/flavinus_400.png"))

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.frame_rate = frame_rate
        self.grid = None
        self.paused = False
        self.running = False


    def start(self, grid: LifeGrid):
        self.grid = grid
        self.running = True
        self.paused = False

        while self.running:
            #print(f"[ Game of life ] Iteration={self.grid.iteration} Cells={len(self.grid.cells)}")
            self.draw()
            self.handle_events()

            if not self.paused and self.grid.evolve() == 0:
                print("ERROR: No more alive cells !!! 😵")
                self.running = False

            self.clock.tick(self.frame_rate)

        pygame.quit()

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.paused = not self.paused
        if keys[pygame.K_UP]:
            self.frame_rate = min([20, self.frame_rate + 1])
        if keys[pygame.K_DOWN]:
            self.frame_rate = max([1, self.frame_rate - 1])
        elif keys[pygame.K_ESCAPE]:
            self.running = False


    def draw(self):
        self.screen.fill(BG_COLOR)
        for cell in self.grid.cells:
            pygame.draw.rect(self.screen, CELL_COLOR, pygame.Rect(cell[0] * CELL_SIZE, cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()


    def get_bounds(self):
        return (0, 0, round(self.screen.get_width() / CELL_SIZE), round(self.screen.get_height() / CELL_SIZE))
