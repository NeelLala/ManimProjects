from manim import *

class SpiralSquares(Scene):
    def construct(self):
        self.spiral_squares()

    def spiral_squares(self):
        num_squares = 13  # Number of squares in the pattern
        size_factor = 3  # Size factor of the squares
        rotation_speed = 0.1  # Speed of rotation

        for i in range(num_squares):
            square = Square(side_length=1 * size_factor, color=BLUE)
            square.rotate(i * rotation_speed * TAU, about_point=ORIGIN)
            self.play(SpinInFromNothing(square))
            size_factor *= 0.8  # Decrease size for subsequent squares

        self.wait()

