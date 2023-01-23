from kivy.uix.screenmanager import Screen
from fire_admin import auth_login
from fire_admin import db

global_token = None


class LoginScreen(Screen):
    def login(self):
        """
        Function will authenticate users who have already created an account.
        """
        print("Logging in")
        email = self.manager.current_screen.ids.login_email.text
        password = self.manager.current_screen.ids.login_password.text
        global_token = auth_login(email=email, password=password)
        print(f"\n{global_token}")
        ref = db.reference("token/")
        ref.set(global_token)

        self.manager.current = "home_screen"
