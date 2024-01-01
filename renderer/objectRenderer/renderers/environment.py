import pygame
from pygame.locals import *

from ..baseRenderer import BaseRenderer, SimulationObject

from simulation.objects.objectManager import environment

class EnvironmentRenderer(BaseRenderer):
    def draw(self, window, object: SimulationObject):
        super().draw(window, object)
        if not isinstance(object, environment.Environment):
            raise TypeError("Object must be of type Environment")
        pygame.draw.rect(window.dsp, (34, 110, 220),
                         (0, 0, window.w, window.h))