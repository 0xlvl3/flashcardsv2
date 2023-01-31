# Kivy / GUI.
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder

# Logout will log user out when application closes through on_stop.
from fire_admin import logout

# Helper function.
from helper import switch_theme

# Screens imports.
from screens.startscreen import StartScreen
from screens.createscreen import CreateScreen
from screens.loginscreen import LoginScreen
from screens.homescreen import HomeScreen
from screens.createdeckscreen import CreateDeckScreen
from screens.addflashcardscreen import AddFlashcardScreen
from screens.inspectdeckscreen import InspectDeckScreen
from screens.deletedeckscreen import DeleteDeckScreen
from screens.playdeckscreen import PlayDeckScreen


# Root kv file.
class RootWidget(MDScreenManager):
    Builder.load_file("kv/root.kv")


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.TOKEN = ""

    def set_theme(self, theme, primary, accent):
        self.theme_cls.theme_style = theme
        self.theme_cls.primary_palette = primary
        self.theme_cls.accent_palette = accent

    def check(self, checkbox, value):
        if value:
            print("Dark")
            MDApp.get_running_app().set_theme("Dark", "LightGreen", "LightGreen")
        if not value:
            print("Light")
            MDApp.get_running_app().set_theme("Light", "Orange", "Orange")

    def build(self):
        self.set_theme("Light", "Orange", "Orange")
        self.theme_cls.primary_hue = "A400"
        return RootWidget()

    def on_stop(self):
        home_screen = self.root.get_screen("home_screen")
        user_token = home_screen.token
        logout(user_token)


if __name__ == "__main__":
    MainApp().run()
