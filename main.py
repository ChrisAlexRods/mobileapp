from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from challenges import challenges, generate_challenge

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

        layout = BoxLayout(orientation='vertical')

        self.level_label = Label(text=f"Level: {self.character.level}")
        layout.add_widget(self.level_label)

        self.xp_label = Label(text=f"XP: {self.character.xp}")
        layout.add_widget(self.xp_label)

        self.challenge_label = Label(text="Challenge: ")
        layout.add_widget(self.challenge_label)

        complete_button = Button(text='Complete')
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
        self.update_challenge()

if __name__ == '__main__':
    SelfImprovementApp().run()
