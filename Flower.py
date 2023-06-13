from manim import *

class Flower(Scene):
    def construct(self):
        self.draw_flower()

    def draw_flower(self):
        a = 2.5  # Scaling factor
        theta_values = np.linspace(0, 2 * PI, 1000)  # Generate theta values

        # Draw petals for r = a*sin(2θ)
        petal_curve_1 = ParametricFunction(lambda t: np.array([a * np.sin(2 * t) * np.cos(t), a * np.sin(2 * t) * np.sin(t), 0]),
                                           t_range=[0, 2 * PI],
                                           color=BLUE,
                                           stroke_width=4)
        self.play(Create(petal_curve_1))

        petal_curve_2 = ParametricFunction(lambda t: np.array([a * np.sin(4 * t) * np.cos(t), a * np.sin(4 * t) * np.sin(t), 0]),
                                           t_range=[0, 2 * PI],
                                           color=PURPLE,
                                           stroke_width=4)
        self.play(Create(petal_curve_2))

        # Draw petals for r = a*cos(4θ)
        petal_curve_4 = ParametricFunction(lambda t: np.array([a * np.cos(4 * t) * np.cos(t), a * np.cos(4 * t) * np.sin(t), 0]),
                                           t_range=[0, 2 * PI],
                                           color=RED,
                                           stroke_width=4)
                                           
        self.play(Create(petal_curve_4))

        self.wait()

