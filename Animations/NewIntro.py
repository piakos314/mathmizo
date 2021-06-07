
from manim import *

class MathMizoLOGO(Scene):
    def construct(self):
        #colors
        self.camera.background_color = BLACK
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"

        #object colors
        mcolor = WHITE
        athcolor = BLUE_C
        izocolor = TEAL_C

        #starting objects
        circle = Circle(color=YELLOW_D, stroke_width = 5).rotate(TAU/8).scale(1.15)
        square = Square(color=BLUE_D, stroke_width = 5).scale(1.15)
        triangle = Triangle(color=GREEN_D, stroke_width = 5).scale(1.15)
        line1 = Line(start=2*LEFT, end=2*RIGHT, color=RED_D, stroke_width = 5).scale(1).shift(0.2*DOWN)

        #logo objects
        #M surrounded my a square
        ds_m = MathTex(r"\mathbb{M}", fill_color=mcolor).scale(9).shift(LEFT)
        #sqr = Rectangle(color = WHITE, height = ds_m.get_height()+0.2,width=ds_m.get_width()+0.2, fill_opacity=0.6).move_to(ds_m)
        m = VGroup(ds_m).shift(LEFT)

        #th sur triangle
        ds_n = Tex(r"{th}", fill_color=athcolor).scale(4)
        #tri = Triangle(color=GREEN_B, fill_opacity=0.5).scale(0.7).shift(ds_n.get_corner(LEFT)+0.3*DOWN+0.05*RIGHT)
        tri = Triangle(color = athcolor, fill_opacity = 0.3).shift(ds_n.get_center()+0.2*UP+0.1*LEFT).scale(1.6)
        ath = VGroup(tri, ds_n).shift(ds_m.get_corner(RIGHT)+1.3*RIGHT+1.3*DOWN).scale(0.9)

        #iz sur circle
        ds_o = Tex(r"iz", fill_color=izocolor).scale(4)
        cir = Circle(color = izocolor, fill_opacity=0.3).surround(ds_o, buffer_factor=1.1).shift(0.1*DOWN)
        izo = VGroup(ds_o, cir).shift(ds_m.get_corner(RIGHT)+2.7*DOWN+1*LEFT)
       
        #grouping
        logo1 = VGroup(m, ath, izo).scale(0.7)  # order matters
        logo1.move_to(ORIGIN)

        #surrounding curve
        surround_curves = [ 
            CircleCurvy(color = MAROON_D),
            CircleCurvy(color = GOLD_D, phase = PI/2),
            CircleCurvy(color = PURPLE_D, phase = PI),
            CircleCurvy(color = RED_D, phase = 3 * PI/2)
        ]
        surround_curve = VGroup(*[x for x in surround_curves]).move_to(ORIGIN).rotate(-PI/8)
        surround_curve.shift(0.15*LEFT + 0.35*UP)

        #ending line
        line = Line(start=2*LEFT, end=2*RIGHT).shift(logo1.get_center())

        #whole thing
        combined = VGroup(surround_curve, logo1).scale(0.8).move_to(ORIGIN)

        colors = [BLUE_D, TEAL_D, BLUE_D]
        colors2 = [PURPLE, MAROON, PURPLE]
        mathmizo = Text("MathMizo").scale(1).set_color_by_gradient(*colors).move_to(ORIGIN).shift(1.5*DOWN)
        comming = Text("coming soon").scale(0.8).set_color_by_gradient(*colors2).move_to(ORIGIN).shift(1.5*DOWN)
        comming1 = Text("coming soon.").scale(0.8).set_color_by_gradient(*colors2).move_to(ORIGIN).shift(1.5*DOWN)
        comming2 = Text("coming soon..").scale(0.8).set_color_by_gradient(*colors2).move_to(ORIGIN).shift(1.5*DOWN)
        comming3 = Text("coming soon...").scale(0.8).set_color_by_gradient(*colors2).move_to(ORIGIN).shift(1.5*DOWN)
        
        #
        #
        # animation starts here
        self.add(combined)
        self.wait(0.017)
        self.remove(combined)
        self.wait(0.3)
        self.play(Write(line1), run_time=0.5)
        self.play(ReplacementTransform(line1, triangle), run_time=0.5)
        self.play(ReplacementTransform(triangle, square), run_time=0.5)
        self.play(ReplacementTransform(square, circle), run_time=0.5)
        self.play(ReplacementTransform(circle, surround_curve), run_time=0.8, rate_func = rate_functions.ease_in_out_sine)

        # logo surround already introduced.
        # logo transformation
        self.play(
            Create(logo1),
            surround_curves[0].animate.rotate(-PI/8),
            surround_curves[1].animate.rotate(PI/8),
            surround_curves[2].animate.rotate(-PI/8),
            surround_curves[3].animate.rotate(PI/8),
            run_time=2.8, rate_func = rate_functions.ease_in_out_sine)
        self.wait(0.5)

        # MathMizo wordings to "continue..."
        self.play(combined.animate.scale(0.5).shift(0.5*UP), FadeInFrom(mathmizo, ORIGIN+3*DOWN), run_time  = 0.5)
        self.wait(1.2)
        self.play(TransformMatchingShapes(mathmizo, comming, path_arc = PI/2), run_time = 0.5)
        self.play(TransformMatchingShapes(comming, comming1), run_time=0.3)
        self.play(TransformMatchingShapes(comming1, comming2), run_time=0.3)
        self.play(TransformMatchingShapes(comming2, comming3), run_time=0.3)
        self.wait(0.8)
        end = VGroup(combined, comming3)
        self.play(ReplacementTransform(end, line), run_time=0.3)

        #shutter effect
        self.wait(0.1)
        self.remove(line)
        self.wait(0.1)
        self.add(line)
        self.wait(0.1)
        self.remove(line)
        self.wait(0.1)
        self.add(line)
        self.wait(0.2)
        self.play(Uncreate(line), run_time=0.2)
        self.wait(0.2)        

      

        ''' # this section is for generating the image
        reall = VGroup(circle1, logo1)
        self.add(reall)'''
    