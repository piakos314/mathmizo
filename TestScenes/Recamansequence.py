from manim import *


class RecamanSequence(MovingCameraScene):
    n = 100

    def construct(self):
        VIBGYOR = [PURPLE, MAROON, BLUE, GREEN, YELLOW, ORANGE, RED]
        self.count = 0
        visited = [0] + [None] * self.n
        arcs = VGroup()

        self.index = 0  # acts as a pointer
        self.highest = max(self.index, 3)  # use to define the frame width

        for i in range(self.n):
            index = self.index - self.count

            if index < 0 or index in visited:
                index = self.index + self.count

            # defining the start and end of the arc
            start = np.array([visited[self.count], 0, 0])
            end = np.array([index, 0, 0])

            # defining the angle of arc (i.e., upwards arc or downwards arc)
            angle = -PI if self.count % 2 == 0 else PI

            if index < visited[self.count]:
                angle *= -1

            arc = ArcBetweenPoints(start, end, angle, stroke_width = 50)
            arcs.add(arc)

            # updating variables
            self.index = index
            self.count += 1
            visited[self.count] = self.index

        VIBGYOR.reverse()

        arcs.set_color_by_gradient(*VIBGYOR)

        # rendering
        for i, arc in enumerate(arcs):
            self.highest = max(self.highest, max(visited[:i+2]))
            arc.set_stroke(opacity=1 - (np.sqrt(i)/self.n))

            #self.play(self.camera.frame.animate.set(width = self.highest))

            self.play(
                Create(arc),                 
                self.camera.frame.animate.move_to(self.highest/2 * RIGHT).set(width = self.highest + 1),                 
                rate_func=linear,
                run_time=0.25
            )
        self.wait(2)