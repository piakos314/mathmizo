from manim import *
import numpy as np

class TestObj(VMobject):
    def __init__(self,**kwargs):
        VMobject.__init__(self,**kwargs)  
        x = np.arange(0, np.pi*4, 0.01)
        points = [np.array([i,np.sin(i),0]) for i in x]
        self.set_points_smoothly(points)

class ObjTest(Scene):
    def construct(self):
        xxx = TestObj().move_to(LEFT)
        self.play(Create(xxx)) #videos
        self.add(xxx) #images
