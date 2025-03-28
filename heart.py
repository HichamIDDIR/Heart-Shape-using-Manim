from manim import *
import numpy as np
from manim.utils.rate_functions import ease_in_out_sine

class SmoothHeart(Scene):
    def construct(self):
        # Define the heart shape using a parametric function
        heart = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t)**3,
                13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t),
                0
            ]),
            t_range=(0, TAU, TAU/1000),  # High resolution for smoothness
            fill_opacity=0,              # No fill, just the outline
            stroke_color=RED,
            stroke_width=4               # Thicker red line
        )

        # Scale and center the heart so it fits nicely on the screen
        heart.scale(0.15)
        heart.move_to(ORIGIN)

        # Animate the drawing of the heart smoothly
        self.play(Create(heart, run_time=5, rate_func=ease_in_out_sine))
        self.wait(2)

