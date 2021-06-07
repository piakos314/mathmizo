from manim import *

class TestTransform(Scene):
	def construct(self):
		cir = Circle(color = BLUE_C)
		sir = CircleCurvy(color = BLUE_C, frequency=10, phase=PI/2).rotate(PI/2)
		self.play(Create(cir), Write(sir), run_time=3)
		self.play(sir.animate.set_color(RED).scale(0.8))
		self.wait()
