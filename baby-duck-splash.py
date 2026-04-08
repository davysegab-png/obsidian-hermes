from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

config.quality = "medium_quality"
config.output_file = "baby_duck_splash"

class BabyDuckSplash(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

        yellow = "#FFD700"
        orange = "#FF8C00"
        light_blue = "#ADD8E6"
        deep_blue = "#006994"
        water_blue = "#1E90FF"
        pink = "#FF69B4"

        # === Title ===
        title = Text("Splash Splash Splash", font_size=56, color=yellow)
        title.shift(UP * 0.5)

        with self.voiceover(text="Splash Splash Splash. A Baby Duck Story."):
            self.play(Write(title))
            self.wait(1)

        self.play(FadeOut(title))

        # === SCENE 1: Sunny day, baby duck is HOT ===
        sky = FullScreenRectangle()
        sky.set_fill(light_blue, opacity=1)
        self.add(sky)

        # Hot sun
        sun = Circle(radius=0.5, color="#FFFF00", fill_opacity=1)
        sun.to_corner(UP + RIGHT, buff=1)

        # Ground
        ground = Rectangle(width=14, height=1.5, color="#228B22", fill_opacity=1)
        ground.shift(DOWN * 3.5)

        # Puddle
        puddle = Ellipse(width=3, height=0.8, color=water_blue, fill_opacity=0.8)
        puddle.shift(DOWN * 2.5)

        self.add(sky, sun, ground, puddle)

        # Baby duck
        duck_body = Ellipse(width=1.2, height=0.9, color=yellow, fill_opacity=1)
        duck_head = Circle(radius=0.45, color=yellow, fill_opacity=1)
        duck_head.shift(np.array([-0.5, 0.5, 0]))
        beak = Polygon([-0.9, 0.5, 0], [-1.1, 0.45, 0], [-0.9, 0.4, 0],
                       fill_opacity=1, fill_color=orange, stroke_opacity=0)
        eye = Circle(radius=0.08, color=BLACK, fill_opacity=1)
        eye.shift(np.array([-0.6, 0.65, 0]))
        duck = VGroup(duck_body, duck_head, beak, eye)
        duck.shift(np.array([-3, -2, 0]))

        self.add(duck)
        self.wait(1)

        # Baby duck is HOT
        hot_text = Text("SO HOT TODAY!", font_size=36, color=yellow)
        hot_text.to_edge(UP)

        with self.voiceover(text="Baby Duck was SO hot today."):
            self.play(Write(hot_text))
            self.wait(1)

        with self.voiceover(text="The sun was big. And bright."):
            self.play(sun.animate.scale(1.3), run_time=1.0)
            self.wait(1)
            self.play(sun.animate.scale(1.0), run_time=0.5)

        with self.voiceover(text="Baby Duck saw a little puddle."):
            self.play(FadeOut(hot_text))
            hot_text2 = Text('"A puddle!"', font_size=34, color=yellow)
            hot_text2.to_edge(UP)
            self.play(Write(hot_text2))
            duck_small = duck.copy()
            self.play(duck_small.animate.move_to(puddle.get_center() + DOWN * 0.3))
            self.wait(1)
            self.play(FadeOut(hot_text2))

        # === SCENE 2: Baby duck jumps in ===
        splash_text = Text("SPLASH!", font_size=48, color=water_blue)

        with self.voiceover(text="So Baby Duck jumped in!"):
            # Jump animation
            self.play(
                duck.animate.move_to(puddle.get_center()).scale(1.2),
                run_time=0.8,
                rate_func=rush_into
            )
            self.wait(0.3)
            self.play(Write(splash_text))
            self.wait(0.5)

        # Water droplets
        for i in range(8):
            angle = (i / 8) * 2 * PI
            drop = Circle(radius=0.15, color=water_blue, fill_opacity=0.8)
            drop.move_to(puddle.get_center())
            with self.voiceover(text="Splash"):
                self.play(
                    drop.animate.shift(UP * 1.5 + RIGHT * 0.5 * (i - 4) * 0.3),
                    run_time=0.4
                )
                self.wait(0.05)

        with self.voiceover(text="Splash splash splash!"):
            splash_text2 = Text("splash splash!", font_size=36, color=water_blue)
            splash_text2.to_edge(DOWN)
            self.play(Transform(splash_text, splash_text2))
            self.wait(0.5)

        self.play(FadeOut(splash_text))

        # === SCENE 3: Taytay calls from the big pond ===
        big_pond = Ellipse(width=6, height=2.5, color=deep_blue, fill_opacity=0.8)
        big_pond.shift(np.array([3, -1.5, 0]))

        taytay = duck.copy().scale(1.15)
        taytay.move_to(big_pond.get_center() + LEFT * 1.5 + UP * 0.3)

        self.play(Create(big_pond))
        self.add(taytay)

        with self.voiceover(text="But TayTay Duck was in the BIG pond."):
            taytay_says = Text('"Hey! That puddle is too small!"', font_size=28, color=pink)
            taytay_says.to_edge(UP)
            self.play(Write(taytay_says))
            self.wait(1)
            self.play(FadeOut(taytay_says))

        with self.voiceover(text="Come to the big pond!"):
            taytay_says2 = Text('"Come to the BIG pond!"', font_size=30, color=pink)
            taytay_says2.to_edge(UP)
            self.play(Write(taytay_says2))
            self.wait(1)
            self.play(FadeOut(taytay_says2))

        # === SCENE 4: Baby duck walks to big pond ===
        walk_text = Text("OK!", font_size=32, color=yellow)
        walk_text.to_edge(UP)

        with self.voiceover(text="OK! Said Baby Duck."):
            self.play(Write(walk_text))
            self.wait(0.5)

        self.play(FadeOut(walk_text))

        # Walk path
        for x in np.linspace(-3, 2, 5):
            with self.voiceover(text="Waddle waddle waddle..."):
                self.play(
                    duck.animate.move_to(np.array([x, -1.5, 0])).scale(1.05),
                    run_time=0.6
                )
                self.wait(0.3)

        # === SCENE 5: Baby duck jumps in the big pond ===
        big_splash = Text("BIG SPLASH!", font_size=52, color=deep_blue)

        with self.voiceover(text="And jumped in!"):
            self.play(
                duck.animate.move_to(big_pond.get_center() + RIGHT * 0.5).scale(1.3),
                run_time=0.8,
                rate_func=rush_into
            )
            self.wait(0.3)
            self.play(Write(big_splash))

        # Big water rings
        for r in [0.3, 0.6, 1.0, 1.5]:
            ring = Circle(radius=r, color=WHITE, fill_opacity=0)
            ring.set_stroke(width=3)
            ring.move_to(big_pond.get_center() + RIGHT * 0.5)
            with self.voiceover(text="Splash!"):
                self.play(Create(ring), run_time=0.4)
                self.wait(0.1)

        with self.voiceover(text="Splash splash splash splash SPLASH!"):
            big_splash2 = Text("splash splash splash!", font_size=36, color=deep_blue)
            big_splash2.to_edge(DOWN)
            self.play(Transform(big_splash, big_splash2))
            self.wait(1)
        self.play(FadeOut(big_splash))

        # === SCENE 6: They're both happy ===
        happy = Text("Happy Duck!", font_size=44, color=yellow)
        happy.move_to(np.array([0, 1, 0]))

        with self.voiceover(text="Two happy ducks in the big pond."):
            both = VGroup(duck, taytay)
            self.play(duck.animate.move_to(big_pond.get_center() + RIGHT * 0.5))
            self.play(taytay.animate.move_to(big_pond.get_center() + LEFT * 1))
            self.play(Write(happy))
            self.wait(1.5)

        # Wiggling in water
        with self.voiceover(text="Wiggle wiggle wiggle."):
            self.play(both.animate.scale(1.05), run_time=0.3)
            self.play(both.animate.scale(0.95), run_time=0.3)
            self.play(both.animate.scale(1.05), run_time=0.3)
            self.play(both.animate.scale(1.0), run_time=0.3)
            self.wait(0.5)

        # === THE END ===
        self.play(FadeOut(happy))
        end = Text("THE END", font_size=60, color=yellow)

        with self.voiceover(text="The End."):
            self.play(Write(end))
            self.wait(2)
