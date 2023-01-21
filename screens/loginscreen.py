from kivy.uix.screenmanager import Screen
from firebase import user_login


class LoginScreen(Screen):
    def login(self):
        """
        Function will authenticate users who have already created an account.
        """
        print("Logging in")
        email = self.manager.current_screen.ids.login_email.text
        password = self.manager.current_screen.ids.login_password.text
        user_login(email, password)
        self.manager.current = "home_screen"
