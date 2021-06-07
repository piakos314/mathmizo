from manim import *

class MathMizo(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"

        ds_m = MathTex(r"\mathbb{M}", fill_color=TEAL_B).scale(8.7)
        ds_n = Tex(r"\underline{ath}", fill_color=GREEN_B).scale(4).shift(2.3*UP+RIGHT)
        ds_o = Tex("izo", fill_color=TEAL_B).scale(4).shift(0.67*UP+RIGHT)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)

        circle = Circle(color=logo_green).rotate(TAU/8)
        square = Square(color=logo_blue)
        triangle = Triangle(color=logo_red)
        line1 = Line(start=2*LEFT, end=2*RIGHT, color=YELLOW_D)
        

        logo1 = VGroup(ds_m, ds_n, ds_o).scale(0.7)  # order matters
        logo2 = VGroup(triangle, square, circle)    
        #logo = VGroup(circle1, logo1).scale(0.8)
        logo1.move_to(ORIGIN)
        circle1 = Circle(color=GREEN_B, fill_color=BLACK, fill_opacity=0, stroke_width = 7).surround(logo1, buffer_factor=1).shift(0.1*LEFT)
        #circle1.set_color_by_gradient([logo_green, logo_blue])

        line = Line(start=2*LEFT, end=2*RIGHT).shift(logo1.get_center())
        
        self.wait(0.2)
        self.play(Write(line1), run_time=0.5)
        self.play(ReplacementTransform(line1, triangle), run_time=0.5)
        self.play(ReplacementTransform(triangle, square), run_time=0.5)
        self.play(ReplacementTransform(square, circle), run_time=0.5)
        self.play(TransformMatchingShapes(circle, circle1), run_time=0.8)
        self.play(Create(logo1), run_time=4)
        self.wait(1)
        self.play(FadeOut(circle1), run_time=0.3)
        self.play(ReplacementTransform(logo1, line), run_time=0.3)
        self.play(Uncreate(line), run_time=0.3)
        self.wait(0.2)

      

        ''' # this section is for generating the image
        reall = VGroup(circle1, logo1)
        self.add(reall)'''
    