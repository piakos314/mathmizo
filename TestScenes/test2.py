from manim import *

class Axe(GraphScene):
    def construct(self):
        axes = Axes(
            x_range=[-PI,PI],
            y_range=[-PI,PI]
        )
        self.add(axes)
