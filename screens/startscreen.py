from kivy.uix.screenmanager import Screen


class StartScreen(Screen):
    def create_account(self):
        """
        Function take user to create account screen.
        """
        self.manager.current = "create_screen"

    def go_to_login(self):
        """
        Function will take user to login screen
        """
        self.manager.current = "login_screen"
