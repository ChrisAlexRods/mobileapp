from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from challenges import challenges, generate_challenge

Window.clearcolor = (0.2, 0.2, 0.2, 1)  # Set the background color to a darker shade

class Character:
    def __init__(self, level=1, xp=0):
        self.level = level
        self.xp = xp

    def gain_xp(self, xp_earned):
        self.xp += xp_earned
        self.check_level_up()

    def check_level_up(self):
        xp_needed = self.calculate_xp_needed()
        if self.xp >= xp_needed:
            self.level += 1
            self.xp -= xp_needed

    def calculate_xp_needed(self):
        return (self.level * 100) + ((self.level - 1) * 50)

class SelfImprovementApp(App):
    def build(self):
        self.character = Character()

        layout = BoxLayout(orientation='vertical', padding=[20, 20, 20, 20], spacing=10)

        self.level_label = Label(text=f"Level: {self.character.level}", font_size=20, halign="left", valign="middle")
        layout.add_widget(self.level_label)

        self.xp_label = Label(text=f"XP: {self.character.xp}", font_size=20, halign="left", valign="middle")
        layout.add_widget(self.xp_label)

        self.xp_bar = ProgressBar(max=self.character.calculate_xp_needed(), value=self.character.xp, size_hint_y=None, height=20)
        layout.add_widget(self.xp_bar)

        self.challenge_label = Label(text="Challenge: ", font_size=18, halign="left", valign="middle", size_hint_y=None, height=50)
        layout.add_widget(self.challenge_label)

        complete_button = Button(text='Complete', size_hint_y=None, height=50)
        complete_button.bind(on_press=self.complete_challenge)
        layout.add_widget(complete_button)

        self.update_challenge()

        return layout

    def update_challenge(self):
        self.current_challenge = generate_challenge(self.character.level, challenges)
        self.challenge_label.text = f"Challenge: {self.current_challenge['title']}"

    def complete_challenge(self, instance):
        self.character.gain_xp(self.current_challenge['xp'])
        self.level_label.text = f"Level: {self.character.level}"
        self.xp_label.text = f"XP: {self.character.xp}"
        self.xp_bar.max = self.character.calculate_xp_needed()
        self.xp_bar.value = self.character.xp

        self.animate_complete_button(instance)
        self.update_challenge()

    def animate_complete_button(self, instance):
        animation = Animation(background_color=(0.5, 0.5, 0.5, 1), duration=0.2) + Animation(background_color=(1, 1, 1, 1), duration=0.2)
        animation.start(instance)

if __name__ == '__main__':
    SelfImprovementApp().run()
