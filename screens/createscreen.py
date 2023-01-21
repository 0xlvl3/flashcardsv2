from kivy.uix.screenmanager import Screen
from firebase import signup


class CreateScreen(Screen):
    def create(self):
        email = self.manager.current_screen.ids.user_email.text
        password = self.manager.current_screen.ids.user_password.text
        signup(email, password)
        print("Account created")
        self.manager.current = "login_screen"
