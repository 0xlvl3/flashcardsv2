from kivy.uix.screenmanager import Screen


class StartScreen(Screen):
    def create_account(self):
        self.manager.current = "create_screen"

    def go_to_login(self):
        self.manager.current = "login_screen"
