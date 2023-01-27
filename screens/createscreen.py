from kivy.uix.screenmanager import Screen
from fire_admin import signup
import requests
import json


class CreateScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.username = ""

    def error_message(self, message):
        self.manager.current_screen.ids.error.text = message

    def create(self):
        """
        Function will create a user giving them authentication and
        will a backend for Decks to be saved that are created by that
        user.
        """
        self.username = self.manager.current_screen.ids.username.text
        email = self.manager.current_screen.ids.user_email.text
        password = self.manager.current_screen.ids.user_password.text

        try:
            self.user = signup(email, password)
            print("Account created")
            self.manager.current = "login_screen"
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)["error"]
            message = error["message"]
            if message == "INVALID_EMAIL":
                self.error_message("Invalid email, please try again")
            elif message == "MISSING_PASSWORD":
                self.error_message(
                    "Password missing, password should be at least 6 characters"
                )
            elif message == "EMAIL_EXISTS":
                self.error_message("Email is already registered")
            elif "WEAK_PASSWORD" in message:
                self.error_message("Password should be at least 6 characters")
            else:
                self.error_message(message)

    def go_to_login(self):
        self.manager.current = "login_screen"

    def return_home(self):
        """
        Function will return the user back to the start screen.
        """
        self.manager.current = "start_screen"


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
            on_press: root.return_home()
"""
