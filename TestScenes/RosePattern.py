from manim import *
from manim.opengl import *


class RosePattern(VMobject):
    
    

    def __init__(self, 
        k = 3, 
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
                radius * np.cos(k * t) * np.cos(t),
                radius * np.cos(k * t) * np.sin(t),
                0
            ]) for t in theta
        ]
        self.set_points_smoothly(points)

class ChangingPattern(Scene):
	def construct(self):

		def changer(mobj, dt):
			ss = 3.0
			while(ss<=5):
				ss += 0.1
				mobj.set(k = ss)


		rose = RosePattern(k = 3, color = RED).move_to(ORIGIN).set(k=5)

		rose.add_updater(changer)
		self.play(Create(rose))

		self.wait()

class Increasingcircle(Scene):
	def construct(self):
		def increaser(mobj, dt):
			mobj.radius=5

		circ = OpenGLCircle(radius = 1, color = RED)

		self.play(Create(circ))
		#self.play(circ.animate.set(radius=5))
		circ.add_updater(increaser)
		self.wait()


class RosePatternNutshell(Scene):
    num = 5
    offset = 2.3


    def construct(self):
        grps = VGroup()  # as there are going to be groups of Texs and RosePatterns
        texs = VGroup()
        patterns = VGroup()

        for n in range(self.num + 1):
            for d in range(self.num + 1):
                if n == 0 and d == 0:
                    tex = Tex(r"$k = \frac{n}{d}$", font_size=25)
                    grps.add(tex)
                    texs.add(tex)
                if n == 0 and d != 0: 
                    tex = Tex(f"d = {d}", font_size=25)
                    grps.add(tex)
                    texs.add(tex)
                if n != 0 and d == 0:
                    tex = Tex(f"n = {n}", font_size=25)
                    grps.add(tex)
                    texs.add(tex)
                if n != 0 and d != 0:
                    pattern = RosePattern(
                        k=n / d,
                        radius= 15 / (2 * self.offset * (self.num + 1)),
                        theta=2 * self.num * PI)
                    grps.add(pattern)
                    patterns.add(pattern)

        colors = [ORANGE, TEAL, BLUE, GREEN, RED, MAROON, PURPLE, PINK]

        grps.arrange_in_grid(fill_rows_first=False)
        patterns.set_color_by_gradient(*colors)
        texs.set_color_by_gradient(*colors)

        self.play(*[Write(tex) for tex in texs])
        self.play(
            *[Create(pattern) for pattern in patterns],
            run_time=8,
            rate_func=linear
        )
        self.wait()
