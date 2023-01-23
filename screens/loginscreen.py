from kivy.uix.screenmanager import Screen
from fire_admin import log_user


class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.token = ""

    def login(self):
        """
        Function will authenticate users who have already created an account.
        """
        print("Logging in")
        email = self.manager.current_screen.ids.login_email.text
        password = self.manager.current_screen.ids.login_password.text
        logged_user = log_user(email, password)
        self.token = logged_user["idToken"]
        print(f"\n{self.token}")
        self.manager.current_screen.ids.home.text = "Click to go to home"

    def get_token(self):
        return self.token

    def go_to_home(self):
        self.manager.current = "home_screen"
        self.manager.get_screen("home_screen").token = self.token
