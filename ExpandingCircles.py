from manim import *
import random

class ExpandingCircles(Scene):
    def construct(self):
        self.expanding_circles()

    def expanding_circles(self):
        num_circles = 10  # Number of circles in the pattern
        initial_radius = 0.5  # Initial radius of the circles
        radius_increment = 0.2  # Increment in radius for subsequent circles

        for i in range(num_circles):
            circle = Circle(radius=initial_radius + i * radius_increment, color=random_color())
            self.play(Create(circle))
            self.play(GrowFromCenter(circle))
        self.wait(2)

def random_color():
    return random.choice([RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE])  # Colour palette

