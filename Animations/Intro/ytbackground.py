from manim import *

class BgWave(VMobject): #user defined
    def __init__(
        self,
        theta = 2*PI*2,
        step_size =0.05,
        amplitude = 1,
        radius = 3.2,
        frequency = 3,
        phase = 0,
        **kwargs):
        '''
        self.theta = theta
        self.step_size = step_size
        self.amplitude = amplitude'''
        super().__init__(self, **kwargs)

        theta = np.arange(0, theta+step_size, step_size)
        points = [np.array([
            t*(4/PI), 
            amplitude * np.sin(phase+ frequency * t), 0])
            for t in theta]

        self.set_points_smoothly(points)

class BGIMAGE(Scene):
    def construct(self):
        waves = [
            BgWave(color = RED_D),
            BgWave(color = GOLD_D, phase=PI/2),
            BgWave(color = MAROON_D, phase = PI),
            BgWave(color = PURPLE_D, phase = 3* PI/2)
        ]
        wave = VGroup(*[x for x in waves]).move_to(ORIGIN)
        self.add(wave)