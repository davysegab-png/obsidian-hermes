from manim import *
import numpy as np

config.quality = "medium_quality"
config.output_file = "baby_duck_up"

class BabyDuckGoesUp(Scene):
    def construct(self):
        # Colors
        yellow = "#FFD700"
        orange = "#FF8C00"
        blue_sky = "#87CEEB"
        green_hill = "#228B22"
        dark_green = "#006400"
        sun_color = "#FFFF00"

        # === SCENE 1: Title ===
        title = Text("Baby Duck Goes UP", font_size=60, color=yellow)
        title.shift(UP * 0.5)
        self.add(title)

        duck_intro = Text("A Story for a Little One", font_size=28, color=WHITE)
        duck_intro.next_to(title, DOWN)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(duck_intro))

        # === SCENE 2: The Hill ===
        # Sky background
        sky = FullScreenRectangle()
        sky.set_fill(blue_sky, opacity=1)
        self.add(sky)

        # Sun
        sun = Circle(radius=0.4, color=sun_color, fill_opacity=1)
        sun.to_corner(UP + RIGHT, buff=1)
        self.add(sun)

        # Big hill
        hill = Polygon(
            [-7, -2, 0],
            [0, 3, 0],
            [7, -2, 0],
            fill_opacity=1,
            fill_color=green_hill,
            stroke_color=dark_green,
            stroke_width=3
        )
        self.add(hill)

        # Clouds
        for x in [-3, 2, 5]:
            cloud = VGroup(*[Circle(radius=0.4, color=WHITE, fill_opacity=0.8) for _ in range(3)])
            cloud.arrange(buff=0.2)
            cloud.shift(np.array([x, 2.5, 0]))
            self.add(cloud)

        # Baby duck body
        duck_body = Ellipse(width=1.2, height=0.9, color=yellow, fill_opacity=1)
        duck_head = Circle(radius=0.45, color=yellow, fill_opacity=1)
        duck_head.shift(np.array([-0.5, 0.5, 0]))
        duck_body.shift(np.array([0, 0, 0]))

        # Beak
        beak = Polygon([-0.9, 0.5, 0], [-1.1, 0.45, 0], [-0.9, 0.4, 0],
                       fill_opacity=1, fill_color=orange, stroke_opacity=0)

        # Eye
        eye = Circle(radius=0.08, color=BLACK, fill_opacity=1)
        eye.shift(np.array([-0.6, 0.65, 0]))

        duck = VGroup(duck_body, duck_head, beak, eye)
        duck.shift(np.array([-4, -0.5, 0]))

        # Taytay duck (smaller, further back)
        taytay = duck.copy()
        taytay.scale(1.2)
        taytay.shift(np.array([-5.5, -0.2, 0]))

        self.add(hill, duck, taytay)
        self.wait(1)

        # === SCENE 3: Baby duck sees the hill ===
        speech = Text('"I can\'t go up that!"', font_size=32, color=WHITE)
        speech.to_edge(UP)
        self.play(Write(speech))
        self.wait(2)
        self.play(FadeOut(speech))

        # === SCENE 4: Taytay speaks ===
        taytay_says = Text('"Yes you can."', font_size=30, color="#FF69B4")
        taytay_says.to_edge(UP)
        self.play(Write(taytay_says))
        self.wait(1)

        taytay_says2 = Text('"One step. Then another."', font_size=30, color="#FF69B4")
        self.play(Transform(taytay_says, taytay_says2))
        self.wait(1)

        taytay_says3 = Text('"Then another."', font_size=30, color="#FF69B4")
        self.play(Transform(taytay_says, taytay_says3))
        self.wait(1)
        self.play(FadeOut(taytay_says))

        # === SCENE 5: Baby duck climbs ===
        # Step markers on hill
        steps = [
            np.array([-2.5, 0.2, 0]),
            np.array([-1.5, 1.0, 0]),
            np.array([-0.5, 1.8, 0]),
            np.array([0.3, 2.5, 0]),
        ]

        # Baby duck walks up step by step
        for i, pos in enumerate(steps):
            step_circle = Circle(radius=0.2, color=WHITE, fill_opacity=0.5)
            step_circle.move_to(pos)
            self.play(Create(step_circle), run_time=0.3)

            # Jump up animation
            self.play(
                duck.animate.move_to(pos).scale(1 + 0.05 * (3 - i)),
                run_time=0.8,
                rate_func=there_and_back
            )
            self.wait(0.3)

        # === SCENE 6: At the top! ===
        # Celebratory burst
        for angle in np.linspace(0, 2 * PI, 8):
            burst = Line(UP * 0.3, UP * 0.6)
            burst.rotate(angle)
            burst.move_to(duck.get_center())
            burst.set_color(yellow)
            self.play(Create(burst), run_time=0.2)

        celebration = Text("I DID IT!", font_size=48, color=yellow)
        celebration.move_to(np.array([0, 1, 0]))
        self.play(Write(celebration))
        self.wait(1.5)

        # Taytay cheers
        taytay_says4 = Text('"You DID IT!"', font_size=32, color="#FF69B4")
        taytay_says4.to_edge(UP)
        self.play(Write(taytay_says4))
        self.wait(1)
        self.play(FadeOut(taytay_says4))

        # === SCENE 7: Baby duck laughs all the way down ===
        laugh = Text("Ha ha ha!", font_size=36, color=yellow)
        laugh.move_to(np.array([0, 1.5, 0]))

        # Bounce down
        for pos in reversed(steps[:-1]):
            self.play(
                duck.animate.move_to(pos),
                run_time=0.6,
                rate_func=rush_into
            )
            self.play(Write(laugh), run_time=0.2)
            self.wait(0.2)

        # Back to bottom
        self.play(duck.animate.move_to(np.array([-4, -0.5, 0])), run_time=0.8)
        self.wait(0.5)

        # === THE END ===
        self.play(FadeOut(laugh))
        end_card = Text("THE END", font_size=56, color=yellow)
        self.play(Write(end_card))
        self.wait(2)
