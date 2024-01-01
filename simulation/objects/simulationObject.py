import numpy as np

class SimulationObject:
    def __init__(self, xy=np.array([0, 0]), velocity=np.array([0, 0])):
        self.xy = xy
        self.velocity = velocity
        self.parent = None
        self.children = []
    
    def update(self):
        self.position = np.add(self.position, self.velocity)
        for child in self.children:
            child.update()
    
    def set_parent(self, parent):
        self.parent = parent
        self.parent.add_child(self)
    
    def add_child(self, child):
        self.children.append(child)