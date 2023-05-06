import random
from datetime import datetime, timedelta
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from character import Character
from challenges import generate_challenge, challenges
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy3 import Scene, Renderer, PerspectiveCamera
from kivy3.loaders import OBJLoader
from kivy.uix.floatlayout import FloatLayout
import math


def create_3d_heart(self):
    # Set up the 3D scene
    scene = Scene(background_color=(1, 1, 1, 1))
    camera = PerspectiveCamera(pos=(0, 0, 5), up=(0, 1, 0), fov=75)
    renderer = Renderer(scene=scene, camera=camera, size_hint=(1, 1))
    renderer.set_clear_color((1, 1, 1, 1))

    # Load the 3D heart model (in OBJ format)
    loader = OBJLoader()
    heart = loader.load("path/to/heart.obj")
    heart.pos.z = -3
    scene.add(heart)

    # Add ambient light
    ambient_light = AmbientLight(color=(0.3, 0.3, 0.3))
    scene.add(ambient_light)

    # Add point light
    point_light = PointLight(color=(1, 1, 1), pos=(3, 3, 3))
    scene.add(point_light)

    # Rotate and scale animation
    def animate_heart(dt):
        heart.rotation.y += 1
        heart.rotation.z += 1
        heart.scale.x = 1 + 0.1 * math.sin(2 * math.pi * dt)
        heart.scale.y = 1 + 0.1 * math.sin(2 * math.pi * dt)
        heart.scale.z = 1 + 0.1 * math.sin(2 * math.pi * dt)

    Clock.schedule_interval(animate_heart, 1 / 60)

    return renderer


class SelfImprovementApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Change the background color to white
        self.challenges = []
        self.last_generated = datetime.now() - timedelta(minutes=30)
        self.generate_challenges()

        self.character = Character()

        layout = BoxLayout(orientation='vertical', padding=[20, 20, 20, 20], spacing=10)

        self.level_label = Label(text=f"Level: {self.character.level}", font_size=20, halign="left", valign="middle", color=(1, 1, 1, 1))
        layout.add_widget(self.level_label)

        self.xp_label = Label(text=f"XP: {self.character.xp}", font_size=20, halign="left", valign="middle", color=(1, 1, 1, 1))
        layout.add_widget(self.xp_label)

        self.xp_bar = ProgressBar(max=self.character.calculate_xp_needed(), value=self.character.xp, size_hint_y=None, height=20)
        layout.add_widget(self.xp_bar)

        self.challenge_label = Label(text="Challenge: ", font_size=18, halign="left", valign="middle", size_hint_y=None, height=50, color=(1, 1, 1, 1))
        layout.add_widget(self.challenge_label)

        complete_button = Button(text='Complete', size_hint_y=None, height=50, background_color=(0, 0.7, 0.8, 1), font_size=18, color=(1, 1, 1, 1))
        complete_button.bind(on_press=self.complete_challenge)
        layout.add_widget(complete_button)

        # Create a new GridLayout for challenge choices
        self.choices_layout = GridLayout(cols=2, spacing=20, size_hint_y=None, height=200)
        for idx, challenge in enumerate(self.challenges):
            choice_button = Button(text=f"Choice {idx + 1}", size_hint_y=None, height=50, background_color=(0, 0.7, 0.8, 1), font_size=18, color=(1, 1, 1, 1))
            choice_button.bind(on_press=lambda instance, c=challenge: self.select_challenge(instance, c))
            self.choices_layout.add_widget(choice_button)
        layout.add_widget(self.choices_layout)

        self.update_challenge()
        heart_renderer = self.create_3d_heart()
        layout.add_widget(heart_renderer)

        return layout

    def generate_challenges(self):
        if datetime.now() - self.last_generated >= timedelta(minutes=30):
            self.challenges = random.sample(challenges, 4)
            self.last_generated = datetime.now()

    def update_challenge(self):
        self.current_challenge = generate_challenge(self.character.level, self.challenges)
        self.challenge_label.text = f"Challenge: {self.current_challenge['title']}"

    def complete_challenge(self, instance):
        self.character.gain_xp(self.current_challenge['xp'])
        self.level_label.text = f"Level: {self.character.level}"
        self.xp_label.text = f"XP: {self.character.xp}"
        self.xp_bar.max = self.character.calculate_xp_needed()
        self.xp_bar.value = self.character.xp

        self.animate_complete_button(instance)

        # Remove the completed challenge from the list
        self.challenges.remove(self.current_challenge)

        # Add a new challenge to the list
        new_challenge = generate_challenge(self.character.level, challenges)
        while new_challenge in self.challenges:
            new_challenge = generate_challenge(self.character.level, challenges)
        self.challenges.append(new_challenge)

        # Update the choices_layout
        self.choices_layout.clear_widgets()
        for idx, challenge in enumerate(self.challenges):
            choice_button = Button(text=f"Choice {idx + 1}", size_hint_y=None, height=50)
            choice_button.bind(on_press=lambda instance, c=challenge: self.select_challenge(instance, c))
            self.choices_layout.add_widget(choice_button)

        self.update_challenge()


    def animate_complete_button(self, instance):
        animation = Animation(background_color=(0.5, 0.5, 0.5, 1), duration=0.2) + Animation(background_color=(1, 1, 1, 1), duration=0.2)
        animation.start(instance)

    def select_challenge(self, instance, challenge):
        self.current_challenge = challenge
        self.challenge_label.text = f"Challenge: {self.current_challenge['title']}"

if __name__ == '__main__':
    SelfImprovementApp().run()

# ... Remaining code
