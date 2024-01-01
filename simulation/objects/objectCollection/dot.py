import numpy as np

from ..simulationObject import SimulationObject

class Dot(SimulationObject):
    def __init__(self, xy=np.array([0, 0]), velocity=np.array([0, 0]),
                 size=10):
        super().__init__(xy, velocity)
        self.size = size