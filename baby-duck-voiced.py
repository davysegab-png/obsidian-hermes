from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

config.quality = "medium_quality"
config.output_file = "baby_duck_up_voiced"

class BabyDuckGoesUpVoiced(VoiceoverScene):
    def construct(self):
        # Set up TTS - Google Translate TTS (free, no API key)
        self.set_speech_service(GTTSService())

        yellow = "#FFD700"
        orange = "#FF8C00"
        blue_sky = "#87CEEB"
        green_hill = "#228B22"
        dark_green = "#006400"

        # === SCENE 1: Title ===
        title = Text("Baby Duck Goes UP", font_size=56, color=yellow)
        title.shift(UP * 0.5)

        with self.voiceover(text="Baby Duck Goes UP. A story for a little one."):
            self.play(Write(title))
            self.wait(1)

        self.play(FadeOut(title))

        # === SCENE 2: The landscape ===
        sky = FullScreenRectangle()
        sky.set_fill(blue_sky, opacity=1)
        self.add(sky)

        # Sun
        sun = Circle(radius=0.4, color="#FFFF00", fill_opacity=1)
        sun.to_corner(UP + RIGHT, buff=1)

        # Big hill
        hill = Polygon(
            [-7, -2, 0], [0, 3, 0], [7, -2, 0],
            fill_opacity=1, fill_color=green_hill,
            stroke_color=dark_green, stroke_width=3
        )

        # Baby duck
        duck_body = Ellipse(width=1.2, height=0.9, color=yellow, fill_opacity=1)
        duck_head = Circle(radius=0.45, color=yellow, fill_opacity=1)
        duck_head.shift(np.array([-0.5, 0.5, 0]))
        beak = Polygon([-0.9, 0.5, 0], [-1.1, 0.45, 0], [-0.9, 0.4, 0],
                       fill_opacity=1, fill_color=orange, stroke_opacity=0)
        eye = Circle(radius=0.08, color=BLACK, fill_opacity=1)
        eye.shift(np.array([-0.6, 0.65, 0]))
        duck = VGroup(duck_body, duck_head, beak, eye)
        duck.shift(np.array([-4, -0.5, 0]))

        # Taytay duck (bigger, behind)
        taytay = duck.copy().scale(1.15)
        taytay.shift(np.array([-5.5, -0.1, 0]))

        self.add(sky, sun, hill, taytay, duck)
        self.wait(1)

        # === SCENE 3: Baby duck sees the hill ===
        speech_bubble = Text('"I can\'t go up that!"', font_size=32, color=WHITE)
        speech_bubble.to_edge(UP)

        with self.voiceover(text="Baby Duck saw a big, tall hill."):
            self.play(FadeIn(speech_bubble))
            self.wait(1)

        with self.voiceover(text="I can't go up that!"):
            self.play(speech_bubble.animate.set_color("#FFD700"))
            self.wait(1)
        self.play(FadeOut(speech_bubble))

        # === SCENE 4: Taytay speaks ===
        with self.voiceover(text="But TayTay Duck knew something."):
            self.play(taytay.animate.shift(RIGHT * 0.3))
            self.wait(1)

        taytay_says = Text('"Yes you can."', font_size=32, color="#FF69B4")
        taytay_says.to_edge(UP)

        with self.voiceover(text="Yes you can."):
            self.play(Write(taytay_says))
            self.wait(1)

        with self.voiceover(text="One step. Then another."):
            t2 = Text('"One step. Then another."', font_size=30, color="#FF69B4")
            t2.to_edge(UP)
            self.play(Transform(taytay_says, t2))
            self.wait(1.5)

        with self.voiceover(text="Then another."):
            t3 = Text('"Then another."', font_size=30, color="#FF69B4")
            t3.to_edge(UP)
            self.play(Transform(taytay_says, t3))
            self.wait(1)
        self.play(FadeOut(taytay_says))

        # === SCENE 5: Baby duck climbs ===
        steps = [
            np.array([-2.5, 0.2, 0]),
            np.array([-1.5, 1.0, 0]),
            np.array([-0.5, 1.8, 0]),
            np.array([0.3, 2.5, 0]),
        ]

        step_texts = [
            "One step...",
            "Then another...",
            "Keep going...",
            "Almost there...",
        ]

        for i, (pos, step_text) in enumerate(zip(steps, step_texts)):
            step_marker = Circle(radius=0.25, color=WHITE, fill_opacity=0.4)

            with self.voiceover(text=step_text):
                self.play(Create(step_marker.move_to(pos)), run_time=0.2)
                # Hop animation synced to voice
                self.play(
                    duck.animate.move_to(pos),
                    run_time=1.0,
                    rate_func=there_and_back
                )
                self.wait(0.2)

        # === SCENE 6: At the top ===
        celebrate = Text("I DID IT!", font_size=52, color=yellow)
        celebrate.move_to(np.array([0, 1, 0]))

        with self.voiceover(text="I did it!"):
            # Star burst
            for angle in np.linspace(0, 2 * PI, 8):
                burst = Line(UP * 0.3, UP * 0.7)
                burst.rotate(angle)
                burst.move_to(duck.get_center())
                burst.set_color(yellow)
                self.play(Create(burst), run_time=0.15)
            self.play(Write(celebrate), run_time=0.5)
            self.wait(0.5)

        with self.voiceover(text="Yay Duck!"):
            self.play(duck.animate.scale(1.1), run_time=0.3)
            self.play(duck.animate.scale(1.0), run_time=0.3)
            self.wait(0.5)

        # Taytay cheers
        with self.voiceover(text="You did it, Baby Duck!"):
            taytay_cheer = Text('"You DID IT!"', font_size=32, color="#FF69B4")
            taytay_cheer.to_edge(UP)
            self.play(Write(taytay_cheer))
            self.wait(1)
            self.play(FadeOut(taytay_cheer))

        # === SCENE 7: Laughing all the way down ===
        laugh = Text("Ha ha ha!", font_size=40, color=yellow)

        with self.voiceover(text="And Baby Duck laughed all the way down!"):
            laugh.move_to(np.array([0, 1.5, 0]))
            self.play(Write(laugh), run_time=0.3)

            # Bounce down steps
            for pos in reversed(steps[:-1]):
                self.play(
                    duck.animate.move_to(pos),
                    run_time=0.5,
                    rate_func=rush_into
                )
                self.wait(0.3)

            # Back to start
            self.play(duck.animate.move_to(np.array([-4, -0.5, 0])), run_time=0.8)
            self.wait(0.5)

        self.play(FadeOut(laugh))

        # === THE END ===
        end_card = Text("THE END", font_size=60, color=yellow)

        with self.voiceover(text="The End."):
            self.play(Write(end_card))
            self.wait(1.5)
