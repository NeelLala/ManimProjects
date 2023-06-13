from manim import *

class Petals(Scene):
    def construct(self):
        self.draw_petals()

    def draw_petals(self):
        a = 2.5  # Scaling factor
        theta_values = np.linspace(0, 2 * PI, 1000)  # Generate theta values

        # Display the petal equations
        text = MathTex("r = a\\sin 2\\theta")
        text.to_corner(UL)  # Move text to the top left corner
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[0], buff=.1) # Highlight text
        self.play(Create(framebox1))

        # Draw petals for r = a*sin(2θ)
        petal_curve_1 = ParametricFunction(lambda t: np.array([a * np.sin(2 * t) * np.cos(t), a * np.sin(2 * t) * np.sin(t), 0]),
                                           t_range=[0, 2 * PI],
                                           color=BLUE,
                                           stroke_width=4)
        self.play(Create(petal_curve_1))

        self.play(FadeOut(framebox1))

        # Display the petal equations
        text = MathTex("r = a\\cos 4\\theta")
        text.to_corner(RIGHT + UP)  # Move text to the top right corner
        self.play(Write(text))
        framebox2 = SurroundingRectangle(text[0], buff=.1) # Highlight text
        self.play(Create(framebox2))
        
        # Draw petals for r = a*cos(4θ)
        petal_curve_2 = ParametricFunction(lambda t: np.array([a * np.cos(4 * t) * np.cos(t), a * np.cos(4 * t) * np.sin(t), 0]),
                                           t_range=[0, 2 * PI],
                                           color=RED,
                                           stroke_width=4)
        self.play(Create(petal_curve_2))


        self.wait()
        self.play(FadeOut(framebox2))
        self.play(FadeOut(petal_curve_2,petal_curve_1))
        self.wait(1)
        self.play(Rotate(petal_curve_2.shift(LEFT * 4),
                angle=PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(petal_curve_1.shift(RIGHT * 4),
                angle=PI,
                about_point=ORIGIN,
                rate_func=linear,))

        self.wait(5)

