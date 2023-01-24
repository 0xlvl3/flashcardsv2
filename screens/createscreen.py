from kivy.uix.screenmanager import Screen
from fire_admin import signup


class CreateScreen(Screen):
    def create(self):
        """
        Function will create a user giving them authentication and
        will a backend for Decks to be saved that are created by that
        user.
        """
        email = self.manager.current_screen.ids.user_email.text
        password = self.manager.current_screen.ids.user_password.text
        signup(email, password)
        print("Account created")
        self.manager.current = "login_screen"
