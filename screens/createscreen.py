from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from helper import update_text
from helper import get_text
from helper import go_to_screen
from constants import LOGIN_SCREEN
from constants import START_SCREEN
from fire_admin import signup


class CreateScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.username = ""

    def create(self):
        """
        Function will create a user giving them authentication and
        will a backend for Decks to be saved that are created by that
        user.
        """

        # Field inputs to be used in creation of account.

        self.username = get_text(self, "username")
        email = get_text(self, "user_email")
        password = get_text(self, "user_password")

        # If sucess create account, otherwise error will appear in id: error.
        message = self.user = signup(email, password)

        if message == "success":
            print("Account created")
            go_to_screen(self, LOGIN_SCREEN)
        else:
            update_text(self, "error", message)

    def go_to_login(self):
        """
        Function will take user to the login screen.
        """
        go_to_screen(self, LOGIN_SCREEN)

    def return_to_start(self):
        """
        Function will return the user back to the start screen.
        """
        go_to_screen(self, START_SCREEN)


kv_createscreen = """
<CreateScreen>:
    FloatLayout:
        MDLabel:
            id: error
            halign: 'center'
            text: ''
            font_size: 20
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        MDLabel:
            text: "Create Account"
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}
            font_size: 48
        MDTextField:
            id: username
            multiline: False
            write_tab: False
            hint_text: "Username"
            mode: 'rectangle'
            font_size: 18
            size_hint: .4, .11
            pos_hint: {'center_x': .5, 'center_y': .7}
        MDTextField:
            mode: 'rectangle'
            id: user_email
            multiline: False
            write_tab: False
            hint_text: "Email"
            size_hint: .4, .11
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .55}
        MDTextField:
            id: user_password
            password: True
            multiline: False
            write_tab: False
            mode: 'rectangle'
            hint_text: "Password"
            font_size: 18
            size_hint: .4, .11
            pos_hint: {'center_x': .5, 'center_y': .4}
        MDFillRoundFlatButton:
            on_press: root.create()
            text: "Submit"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .25}
            size_hint: .4, .1
        MDFillRoundFlatButton:
            text: "Home"
            pos_hint:{'center_x': .5, 'center_y': .10}
            font_size: 24
            size_hint: .4, .1
            on_press: root.return_to_start()
"""

Builder.load_string(kv_createscreen)
