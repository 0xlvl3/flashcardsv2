# Kivy imports.
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Helper functions.
from helper import go_to_screen

# Constants.
from constants import CREATE_SCREEN
from constants import LOGIN_SCREEN


class StartScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def create_account(self):
        """
        Function take user to create account screen.
        """
        go_to_screen(self, CREATE_SCREEN)

    def go_to_login(self):
        """
        Function will take user to login screen
        """
        go_to_screen(self, LOGIN_SCREEN)


kv_startscreen = """
<StartScreen>
    MDFloatLayout:
        MDSwitch:
            pos_hint: {'center_x': .05, 'center_y': .05}
            width: dp(45)
            on_active: app.check(self, self.active)
        MDLabel:
            id: heading
            text: "kv Flashcards"
            halign: 'center'
            font_size: 56
            pos_hint:{'center_x': .5, 'center_y': .65}
        MDRaisedButton:
            on_press: root.create_account()
            text_color: [0, 0, 0, 1]
            id: 'create_btn'
            text: "Create Account"
            font_size: 24
            size_hint: .4, .1
            pos_hint: {'center_x': .5, 'center_y': .45}
        MDRaisedButton:
            on_press: root.go_to_login()
            text: "Login"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .4, .1
"""

Builder.load_string(kv_startscreen)
