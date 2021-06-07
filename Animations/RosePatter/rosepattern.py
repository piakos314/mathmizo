from manim import *
from manim.opengl import *


class RosePattern(VMobject):
    
    k =3
    

    def __init__(self, 
        k=3, 
        step_size = 0.05,
        theta = 2*PI, 
        radius = 2,
        **kwargs):

        super().__init__(**kwargs)
        theta = np.arange(0, theta + step_size, step_size)

        # Equations:
        # x = a * cos(k * theta) * cos(theta)
        # y = a * cos(k * theta) * sin(theta)
        points = [
            np.array([
                radius * np.cos(self.k * t) * np.cos(t),
                radius * np.cos(self.k * t) * np.sin(t),
                0
            ]) for t in theta
        ]
        self.set_points_smoothly(points)

class Rose(Scene):
    def construct(self):
        rosee = RosePattern(color = RED)
        def increase(mobj, dt):
            mobj.set(k = 5)
        rosee.add_updater(increase)
        self.play(Create(rosee))
        self.play(rosee.animate.scale(5))
        self.wait()