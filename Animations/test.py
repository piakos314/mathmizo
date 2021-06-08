from manim import *

class Crosstest(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        self.stroke_width = 5
        cen = Square(side_length=1, color=BLUE_C, fill_opacity = 0 ,stroke_width = 8)
        part1 = Rectangle(height=2, width=1, color=GREEN_C, fill_opacity = 0.1,stroke_width = 8).move_to(cen.get_corner(UP)).shift(UP)
        part2 = Rectangle(height=4, width=1, color=TEAL_C, fill_opacity = 0.1,stroke_width = 8).move_to(cen.get_corner(DOWN)).shift(2*DOWN)
        part3 = Rectangle(height=1, width=2, color=RED_C, fill_opacity = 0.1,stroke_width = 8).move_to(cen.get_corner(RIGHT)).shift(RIGHT)
        part4 = Rectangle(height=1, width=2, color=GOLD_C, fill_opacity = 0.1,stroke_width = 8).move_to(cen.get_corner(LEFT)).shift(LEFT)
        cor = VGroup(cen, part1, part2, part3, part4).move_to(ORIGIN)
        cir = Circle(color=LIGHT_GRAY, stroke_width = 8).surround(cor, buffer_factor= 0.9)
        self.add(cor, cir)

class bgc(Scene):
    def construct(self):
        p1 = Rectangle(height = 0.6, width = 3, color=GREEN_C).shift(LEFT+ LEFT/2.3 + UP/1.1)
        p2 = Rectangle(height=0.6, width= 2, color=RED_C).shift(RIGHT/1.1)
        p3 = Rectangle(height= 0.7, width=2.4, color=GOLD_C).shift(RIGHT+ RIGHT+ UP)
        p4 = Rectangle(height=0.5, width=1.8, color=BLUE_C).shift(3.5*RIGHT + 0.1* UP)
        pp = VGroup(p1, p2, p3, p4).move_to(ORIGIN).shift(RIGHT*1.2)
        self.add(pp)

class black(Scene):
    def construct(self):
        p1 = Circle(color=BLACK)
        self.add(p1)
        
