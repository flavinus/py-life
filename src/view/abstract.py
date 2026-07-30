from abc import ABC, abstractmethod
from grid import LifeGrid

class ViewInterface(ABC):

    @abstractmethod
    def start(self, grid: LifeGrid):
        pass

    @abstractmethod
    def get_bounds(self):
        pass

    @abstractmethod
    def draw(self):
        pass
