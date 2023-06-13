from manim import *
import random

class LituusCurve(Scene):
    def construct(self):
        self.draw_lituus_curve()

    def draw_lituus_curve(self):
        a = 50  # Constant determining the scale of the curve
        num_points = 1000  # Number of points to trace the curve
        angle_range = np.linspace(1, 5000, num_points)  # Range of angles for the curve

        points = self.get_lituus_points(a, angle_range)
        curve = self.get_lituus_curve(points)
        self.play(Create(curve))
        self.wait(2)

    def get_lituus_points(self, a, angle_range):
        points = []

        for angle in angle_range:
            radius = a / np.sqrt(angle)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            points.append([x, y, 0])

        return points

    def get_lituus_curve(self, points):
        curve = VGroup()

        for i in range(len(points)):
            if i > 0:
                line = Line(points[i - 1], points[i], color=random_color())
                curve.add(line)

        return curve

def random_color():
    return random.choice([RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE])  # Colour palette