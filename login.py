from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Create a vertical layout
        layout = BoxLayout(orientation='vertical')

        # Add a label, text input, and button to the layout
        layout.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        layout.add_widget(self.username)

        layout.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        layout.add_widget(self.password)

        button = Button(text='Login')
        button.bind(on_release=self.login)
        layout.add_widget(button)

        # Add the layout to the screen
        self.add_widget(layout)

    def login(self, instance):
        username = self.username.text
        password = self.password.text

        # Check the username and password
        if username == 'test' and password == 'password':
            # On success, switch to the main game screen
            app = App.get_running_app()
            app.sm.current = 'main'
            return True
        else:
            return False

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super(SignupScreen, self).__init__(**kwargs)

        # Create a vertical layout
        layout = BoxLayout(orientation='vertical')

        # Add a label, text input, and button to the layout
        layout.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        layout.add_widget(self.username)

        layout.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        layout.add_widget(self.password)

        button = Button(text='Sign Up')
        button.bind(on_release=self.signup)
        layout.add_widget(button)

        # Add the layout to the screen
        self.add_widget(layout)

    def signup(self, instance):
        username = self.username.text
        password = self.password.text

        # Add your logic here to register a new user

        # Switch to the main game screen
        app = App.get_running_app()
        app.sm.current = 'main'