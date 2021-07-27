from manim import *

class sample(Scene):
    def construct(self):
        t0 = Text("This is an example for \nreplacement transformations in \nformula derivations")
        self.add(t0)
        self.wait()
        self.play(FadeOut(t0))
        t2 = MathTex(r"{{\frac{2}{2}}} {{=}} {{\lambda}}")
        t3 = MathTex(r"{{\frac{2}{4}}} {{=}} {{\lambda}}")
        eq1 = MathTex("{{a^2}} + {{b^2}} = {{c^2}}")
        eq2 = MathTex("{{a^2}} = {{c^2}} - {{b^2}}")
        eq3 = MathTex("{{a^4}} = {{c^2}} - {{b^2}}")
        self.play(FadeIn(t2))
        self.play(TransformMatchingShapes(t2, t3))
        self.play(FadeOut(t3))
        self.play(Create(eq1))
        self.play(TransformMatchingTex(eq1, eq2))
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait()