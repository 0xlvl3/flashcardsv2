from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemeManager


class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.CURRENT_THEME = MDApp.get_running_app().THEME
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "A200"

    def change_theme(self):
        """
        Function to switch between light and dark theme
        """
        if self.CURRENT_THEME == "Light":
            self.CURRENT_THEME = "Dark"
        else:
            self.CURRENT_THEME = "Light"

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


kv_startscreen = """
<StartScreen>
    FloatLayout:
        MDFillRoundFlatButton:
            text: "change theme"
            font_size: 20
            pos_hint: {'center_x': .2, 'center_y': .9}
            size_hint: .35, .07
            on_press: root.change_theme()
        MDLabel:
            text: "kv Flashcards"
            halign: 'center'
            font_size: 56
            pos_hint:{'center_x': .5, 'center_y': .65}
        MDFillRoundFlatButton:
            on_press: root.create_account()
            text: "Create Account"
            font_size: 24
            size_hint: .4, .1
            pos_hint: {'center_x': .5, 'center_y': .45}
        MDFillRoundFlatButton:
            on_press: root.go_to_login()
            text: "Login"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .4, .1
"""
