from kivy.uix.screenmanager import Screen
from fire_admin import decode_uid
from fire_admin import auth_system
from deck import user_deck
from kivymd.app import MDApp
import requests
import json


class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.token = ""

    def error_message(self, message):
        self.manager.current_screen.ids.error.text = message

    def get_token(self):
        return self.token

    def login(self):
        """
        Function will authenticate users who have already created an account.
        """
        print("Logging in")
        email = self.manager.current_screen.ids.login_email.text
        password = self.manager.current_screen.ids.login_password.text
        try:
            user_logged = auth_system.sign_in_with_email_and_password(email, password)

            self.token = user_logged["idToken"]
            the_user = decode_uid(self.token)
            check = MDApp.get_running_app().logged_token = the_user

            print("logged_token " + check)
            print(f"\n{self.token}")

            print(self.ids)
            self.get_token()

            user_deck.create_deck(the_user, "start_deck")

            self.ids.popup.open()

        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)["error"]
            message = error["message"]
            if "INVALID_EMAIL" in message:
                self.error_message("Invalid email, please try again.")
            elif "MISSING_PASSWORD" in message:
                self.error_message("Password is missing from field.")
            elif "INVALID_PASSWORD" in message:
                self.error_message("Password is incorrect, please try again.")
            elif "EMAIL_NOT_FOUND" in message:
                self.error_message("Email incorrect.")
            elif "TOO_MANY_ATTEMPTS_TRY_LATER" in message:
                self.error_message(
                    "Access temporarily disabled due to too many failed attempts. Please try again later."
                )
            else:
                print(message)

    def go_to_home(self):
        self.manager.current = "home_screen"
        self.manager.get_screen("home_screen").token = self.token


kv_loginscreen = """
<LoginScreen>:
    FloatLayout:
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
                Label:
                    text: "Success!"
                    size_hint: .5, .3
                    font_size: 16
                    pos_hint: {'center_x': .5, 'center_y': .6}
                Button:
                    text: "Home"
                    font_size: 24
                    size_hint: .5, .3
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_press:
                        root.go_to_home()
                        popup.dismiss()
"""
