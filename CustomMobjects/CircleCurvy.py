from manim import *
'''
class CircleCurvy(VMobject):
    def __init__(
        self,
        theta = 2*PI,
        step_size =0.05,
        amplitude = 0.34,
        radius = 3,
        frequency =4,
        phase = 0,
        **kwargs):
        VMobject.__init__(self, **kwargs)
        theta = np.arange(0, theta+step_size, step_size)
        points = [np.array([
            (radius + amplitude * np.sin(phase + frequency * t)) * np.cos(t), 
            (radius + amplitude * np.sin(phase+ frequency * t)) * np.sin(t), 0])
            for t in theta]
        self.set_points_smoothly(points)
'''
class enscene(Scene):
    def construct(self):        
        cir = [
            CircleCurvy(color = RED_D),
            CircleCurvy(color = GOLD_D, phase = PI/2),
            CircleCurvy(color = PURPLE_D, phase = PI),
            CircleCurvy(color = MAROON_D, phase = 3*PI/2)
        ]
        self.add(*[x for x in cir])
        self.play(
            cir[0].animate.rotate(PI/8),
            cir[1].animate.rotate(-PI/8),
            cir[2].animate.rotate(PI/8),
            cir[3].animate.rotate(-PI/8),
            run_time=2, rate_func = rate_functions.ease_in_out_sine
        )
        self.wait()