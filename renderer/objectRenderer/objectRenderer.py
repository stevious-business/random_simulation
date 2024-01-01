import pygame
from pygame.locals import *

from .renderers import dot, environment

from .baseRenderer import BaseRenderer

from simulation.objects import objectManager

NO_OBJ_MGR = """
render() requires window.objectRenderer to have an objectManager.
Set it with win.objRenderer.setObjectMgr(objMgr).
If you haven't created an object manager yet, create an
objectManager.ObjectManager.
"""

class ObjectRenderer:
    def __init__(self, win):
        self.window = win
        self.objectManager = None
    
    def setObjectMgr(self, objMgr):
        self.objectManager = objMgr
    
    def render(self, objlist=None):
        if objlist is None:
            objlist = self.objectManager.objects
        if self.objectManager is None:
            raise ValueError(NO_OBJ_MGR)
        type_to_render_LUT = {
            objectManager.dot.Dot:
                dot.DotRenderer,
            objectManager.environment.Environment:
                environment.EnvironmentRenderer
        }
        for obj in objlist:
            try:
                renderer: BaseRenderer = type_to_render_LUT[type(obj)]()
                renderer.draw(self.window, obj)
            except KeyError:
                raise NotImplementedError("No renderer for type "+type(obj))
            self.render(obj.children)