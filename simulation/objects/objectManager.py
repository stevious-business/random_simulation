from . import simulationObject

from .objectCollection import dot, environment

class ObjectManager:
    def __init__(self):
        self.objects: list[simulationObject.SimulationObject] = []
    
    def addObject(self, object: simulationObject.SimulationObject):
        self.objects.append(object)
    
    def update_all(self):
        for child in self.objects:
            child.update()