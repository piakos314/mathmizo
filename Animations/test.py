from manim import *

class testicle(Scene):
    def construct(self):
        cir = Circle()
        self.play(Create(cir))
        self.wait()