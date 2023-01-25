from kivy.uix.screenmanager import Screen
from fire_admin import signup


class CreateScreen(Screen):
    def create(self):
        """
        Function will create a user giving them authentication and
        will a backend for Decks to be saved that are created by that
        user.
        """
        email = self.manager.current_screen.ids.user_email.text
        password = self.manager.current_screen.ids.user_password.text
        signup(email, password)
        print("Account created")
        self.manager.current = "login_screen"


kv_createscreen = """
<CreateScreen>:
    FloatLayout:
        Label:
            text: "Create Account"
            font_size: 48
            size_hint: .2, .4
            pos_hint:{'center_x':0.5, 'center_y':0.8}
        TextInput:
            id: username
            multiline: False
            write_tab: False
            hint_text: "Username"
            font_size: 16
            size_hint: .4, .05
            pos_hint: {'center_x': .5, 'center_y': .65}
        TextInput:
            id: user_email
            multiline: False
            write_tab: False
            hint_text: "Email"
            size_hint: .4, .05
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .55}
        TextInput:
            id: user_password
            multiline: False
            write_tab: False
            hint_text: "Password"
            font_size: 16
            size_hint: .4, .05
            pos_hint: {'center_x': .5, 'center_y': .45}
        Button:
            on_press: root.create()
            text: "Submit"
            font_size: 32
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .35, .1
"""
