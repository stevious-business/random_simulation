from simulation.objects import objectManager
from renderer.window import Window

def exit_callback(win):
    exit(0)
    # this function can be used to finish up things before exit.

def run_demo():
    win = Window(FPS=60)
    win.configure_terminator(exit_callback, [win,])

    objMgr = objectManager.ObjectManager()

    win.objRenderer.setObjectMgr(objMgr)

    env = objectManager.environment.Environment()

    dot = objectManager.dot.Dot(xy=(100, 100))

    objMgr.addObject(env)

    dot.set_parent(env)

    while True:
        objMgr.update_all()
        win.draw()
        win.update()

run_demo()