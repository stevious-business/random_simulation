import pygame
from pygame.locals import *

from .objectRenderer import objectRenderer

pygame.init()

class Window:
    def __init__(self, wsize=(800, 450), caption="Simulation",
                 tkey=K_ESCAPE, FPS=30):
        self.dsp = pygame.display.set_mode(wsize)
        pygame.display.set_caption(caption)

        self.objRenderer = objectRenderer.ObjectRenderer(self)

        self.terminatorCallback = lambda:0
        self.terminatorArgs = []
        self.terminatorKwArgs = {}
        self.terminatorKey = tkey
        
        self.targetFPS = FPS
        self.clk = pygame.time.Clock()
    
    def configure_terminator(self, fn, args=[], kwargs={}):
        self.terminatorCallback = fn
        self.terminatorArgs = args
        self.terminatorKwArgs = kwargs
    
    def draw(self):


    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT or \
                event.type == KEYDOWN and event.key == self.terminatorKey:
                pygame.quit()
                self.terminatorCallback(
                    *self.terminatorArgs, **self.terminatorKwArgs
                )
        pygame.display.update()
        self.clk.tick(self.targetFPS)