# Kivy / GUI.
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

# Logout will log user out when application closes through on_stop.
from fire_admin import logout


# Screens imports.
from screens.startscreen import kv_startscreen
from screens.createscreen import kv_createscreen
from screens.loginscreen import kv_loginscreen
from screens.homescreen import kv_homescreen
from screens.createdeckscreen import kv_createdeckscreen
from screens.addflashcardscreen import kv_addflashcardscreen
from screens.inspectdeckscreen import kv_inspectdeckscreen
from screens.deletedeckscreen import kv_deletedeckscreen
from screens.playdeckscreen import kv_playdeckscreen

# Root kv file.
Builder.load_string(kv_startscreen)
Builder.load_string(kv_createscreen)
Builder.load_string(kv_loginscreen)
Builder.load_string(kv_homescreen)
Builder.load_string(kv_createdeckscreen)
Builder.load_string(kv_addflashcardscreen)
Builder.load_string(kv_inspectdeckscreen)
Builder.load_string(kv_deletedeckscreen)
Builder.load_string(kv_playdeckscreen)


class RootWidget(ScreenManager):
    Builder.load_file("kv/root.kv")


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.TOKEN = ""

    def check(self, checkbox, value):
        if value:
            print("true")
            self.set_theme("Dark", "Orange", "Orange")
        if not value:
            print("false")
            self.set_theme("Light", "Green", "Green")

    def set_theme(self, theme, primary, accent):
        self.theme_cls.theme_style = theme
        self.theme_cls.primary_palette = primary
        self.theme_cls.accent_palette = accent

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.accent_palette = "LightGreen"
        self.theme_cls.primary_hue = "A200"
        return RootWidget()

    def on_stop(self):
        home_screen = self.root.get_screen("home_screen")
        user_token = home_screen.token
        logout(user_token)


MainApp().run()
