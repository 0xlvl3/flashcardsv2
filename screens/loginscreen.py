# Kivy imports.
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# Firebase imports.
from fire_admin import auth_system
from fire_admin import decode_uid
from fire_admin import user_login

# Module imports.
from deck_module import user_deck

# Helper functions.
from helper import get_text
from helper import update_text
from helper import go_to_screen

# Constants.
from constants import HOME_SCREEN


class LoginScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.token = ""

    def get_token(self):
        return self.token

    def login(self):
        """
        Function will authenticate users who have already created an account.
        """
        print("Logging in")
        email = get_text(self, "login_email")
        password = get_text(self, "login_password")

        # Login.
        message = user_login(email, password)
        if message == "success":

            # On success user will login again to get data.

            user_data = auth_system.sign_in_with_email_and_password(email, password)
            self.token = user_data["idToken"]
            USER_TOKEN = decode_uid(self.token)
            check = MDApp.get_running_app().TOKEN = USER_TOKEN

            print("log token" + check)

            self.get_token()

            # Here we create a deck to initialize the users database.

            user_deck.create_deck(USER_TOKEN, "start_deck")

            self.ids.popup.open()
        else:
            update_text(self, "error", message)

    def go_to_home(self):
        go_to_screen(self, HOME_SCREEN)
        self.manager.get_screen(HOME_SCREEN).token = self.token


kv_loginscreen = """
<LoginScreen>:
    MDFloatLayout:
        id: l_screen
        MDLabel:
            text: "Login"
            font_size: 48
            halign: 'center'
            pos_hint:{'center_x':0.5, 'center_y':0.75}
        MDLabel:
            text: ''
            id: error
            font_size: 16
            halign: 'center'
            pos_hint:{'center_x':0.5, 'center_y':0.65}
        MDTextField:
            mode: 'rectangle'
            id: login_email
            multiline: False
            write_tab: False
            hint_text: "Email"
            size_hint: .4, .11
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .55}
        MDTextField:
            mode: 'rectangle'
            id: login_password
            password: True
            multiline: False
            write_tab: False
            hint_text: "Password"
            font_size: 18
            size_hint: .4, .11
            pos_hint: {'center_x': .5, 'center_y': .4}
        MDFillRoundFlatButton:
            text: "Submit"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .25}
            size_hint: .35, .1
            on_press: root.login()
            on_release: root.get_token()
        MDLabel:
            font_size: 16
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': .15}
            text: 'Forgot password?'
        Popup:
            id: popup
            on_parent: if self.parent == l_screen: l_screen.remove_widget(self)
            title: 'Successful Login'
            content: popupcontent
            size_hint: .7, .7
            pos_hint: {'center_x': .5, 'center_y': .5}
            auto_dismiss: False
            FloatLayout:
                id: popupcontent
                MDLabel:
                    text: "Success!"
                    halign: 'center'
                    font_size: 16
                    pos_hint: {'center_x': .5, 'center_y': .65}
                MDFillRoundFlatButton:
                    text: "Home"
                    font_size: 24
                    size_hint: .4, .1
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_press:
                        root.go_to_home()
                        popup.dismiss()
"""

Builder.load_string(kv_loginscreen)
