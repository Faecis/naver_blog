from manim import *
import numpy as np


class UnitCircle(Scene):
    """
    A Manim scene that visualizes the unit circle and the geometric interpretation
    of trigonometric functions (sine, cosine, secant, cosecant, tangent, and cotangent).
    The scene animates a point rotating around the unit circle and dynamically displays
    the corresponding line segments, braces, and labels for each trigonometric function.
    """
    
    def construct(self):
        """
        Constructs the unit circle animation, including:
        - The unit circle and a rotating point.
        - Points representing projections and intersections for each trig function.
        - Line segments for sine, cosine, tangent, cotangent, secant, and cosecant.
        - Braces and labels for each line segment.
        - An animation that rotates the point around the circle.
        """

        # Circle and theta configuration.

        actual_radius = 2.5
        circle = Circle(radius=actual_radius, color=WHITE)
        theta = ValueTracker(0.0)

        point_origin = Dot(ORIGIN, color=LOGO_WHITE)
        point_circle = always_redraw(
            lambda: Dot([actual_radius*np.cos(theta.get_value()), actual_radius*np.sin(theta.get_value()), 0], color=LOGO_RED)
        )
        point_x_axis = always_redraw(
            lambda: Dot([actual_radius*(1/np.cos(theta.get_value())), 0, 0], color=LOGO_GREEN)
        )
        point_y_axis = always_redraw(
            lambda: Dot([0, actual_radius*(1/np.sin(theta.get_value())), 0], color=LOGO_BLUE)
        )

        # Line segment configuration.

        line_fix = Line(ORIGIN, actual_radius*RIGHT, color=WHITE)
        line_hyp = always_redraw(
            lambda: Line(ORIGIN, [actual_radius*np.cos(theta.get_value()), actual_radius*np.sin(theta.get_value()), 0], color=WHITE)
        )
        line_sin = always_redraw(
            lambda: Line([actual_radius*np.cos(theta.get_value()), 0, 0], [actual_radius*np.cos(theta.get_value()), actual_radius*np.sin(theta.get_value()), 0], color=ORANGE)
        )
        line_cos = always_redraw(
            lambda: Line([0, actual_radius*np.sin(theta.get_value()), 0], [actual_radius*np.cos(theta.get_value()), actual_radius*np.sin(theta.get_value()), 0], color=BLUE)
        )
        line_csc = always_redraw(
            lambda: Line(ORIGIN, [0, actual_radius*(1/np.sin(theta.get_value())), 0], color=PINK)
        )
        line_sec = always_redraw(
            lambda: Line(ORIGIN, [actual_radius*(1/np.cos(theta.get_value())), 0, 0], color=GREEN)
        )
        line_tan = always_redraw(
            lambda: Line([actual_radius*(1/np.cos(theta.get_value())), 0, 0], [actual_radius*np.cos(theta.get_value()), actual_radius*np.sin(theta.get_value()), 0], color=YELLOW)
        )
        line_cot = always_redraw(
            lambda: Line([0, actual_radius*(1/np.sin(theta.get_value())), 0], [actual_radius*np.cos(theta.get_value()), actual_radius*np.sin(theta.get_value()), 0], color=PURPLE)
        )

        # Brace configuration.

        brace_sin = always_redraw(
            lambda: Brace(line_sin, direction=self.get_brace_other_direction(line_sin, theta.get_value()), color=ORANGE)
        )
        brace_cos = always_redraw(
            lambda: Brace(line_cos, direction=self.get_brace_other_direction(line_cos, theta.get_value()), color=BLUE)
        )
        brace_csc = always_redraw(
            lambda: Brace(line_csc, direction=self.get_brace_csc_direction(line_csc, theta.get_value()), color=PINK)
        )
        brace_sec = always_redraw(
            lambda: Brace(line_sec, direction=self.get_brace_other_direction(line_sec, theta.get_value()), color=GREEN)
        )
        brace_tan = always_redraw(
            lambda: Brace(line_tan, direction=self.get_brace_other_direction(line_tan, theta.get_value()), color=YELLOW)
        )
        brace_cot = always_redraw(
            lambda: Brace(line_cot, direction=self.get_brace_other_direction(line_tan, theta.get_value()), color=PURPLE)
        )

        # Brace text configuration.

        label_sin = always_redraw(
            lambda: brace_sin.get_tex(r"\sin(\theta)")
        )
        label_cos = always_redraw(
            lambda: brace_cos.get_tex(r"\cos(\theta)")
        )
        label_csc = always_redraw(
            lambda: brace_csc.get_tex(r"\csc(\theta)")
        )
        label_sec = always_redraw(
            lambda: brace_sec.get_tex(r"\sec(\theta)")
        )
        label_tan = always_redraw(
            lambda: brace_tan.get_tex(r"\tan(\theta)")
        )
        label_cot = always_redraw(
            lambda: brace_cot.get_tex(r"\cot(\theta)")
        )

        # Adding objects to the scene.

        self.add(circle)
        self.add(line_fix, line_hyp, line_sin, line_cos, line_csc, line_sec, line_tan, line_cot)
        self.add(point_origin, point_circle, point_x_axis, point_y_axis)
        self.add(brace_sin, brace_cos, brace_csc, brace_sec, brace_tan, brace_cot)
        self.add(label_sin, label_cos, label_csc, label_sec, label_tan, label_cot)

        # Play animation to rotate the point around the circle.

        self.play(theta.animate.set_value(2*PI), run_time=5.0, rate_func=linear)
    

    def get_brace_csc_direction(self, line: Line, theta: float) -> np.ndarray:
        """
        Determines the direction for the Brace on the cosecant line segment.

        Args:
            line (Line): The line segment representing the cosecant.
            theta (float): The current angle in radians.

        Returns:
            np.ndarray: The direction vector for the Brace.
        """

        theta %= 2 * PI
        angle = 0.0

        if PI/2 <= theta < PI or 3*PI/2 <= theta < 2*PI:
            angle = 3 * PI / 2
        else:
            angle = PI / 2
        
        return line.copy().rotate(angle).get_unit_vector()
    

    def get_brace_other_direction(self, line: Line, theta: float) -> np.ndarray:
        """
        Determines the direction for the Brace on other line segments.

        Args:
            line (Line): The line segment for which the brace is drawn.
            theta (float): The current angle in radians.

        Returns:
            np.ndarray: The direction vector for the Brace.
        """

        theta %= 2 * PI
        angle = 0.0

        if 0.0 <= theta < PI/2 or PI <= theta < 3*PI/2:
            angle = 3 * PI / 2
        else:
            angle = PI / 2

        return line.copy().rotate(angle).get_unit_vector()
