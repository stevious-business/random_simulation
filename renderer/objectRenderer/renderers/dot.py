import pygame
from pygame.locals import *

from ..baseRenderer import BaseRenderer, SimulationObject

from simulation.objects.objectManager import dot

class DotRenderer(BaseRenderer):
    def draw(self, window, object: SimulationObject):
        super().draw(window, object)
        if not isinstance(object, dot.Dot):
            raise TypeError("Object must be of type Dot")
        pygame.draw.circle(window.dsp, (200, 200, 180), object.xy,
                           object.size)