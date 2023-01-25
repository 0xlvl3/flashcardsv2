from kivy.uix.screenmanager import Screen
from fire_admin import log_user
from fire_admin import decode_uid
from kivy.app import App


class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.token = ""

    def login(self):
        """
        Function will authenticate users who have already created an account.
        """
        print("Logging in")
        email = self.manager.current_screen.ids.login_email.text
        password = self.manager.current_screen.ids.login_password.text
        logged_user = log_user(email, password)
        self.token = logged_user["idToken"]
        the_user = decode_uid(self.token)

        check = App.get_running_app().logged_token = the_user

        print("logged_token " + check)
        print(f"\n{self.token}")

    def get_token(self):
        return self.token

    def go_to_home(self):
        self.manager.current = "home_screen"
        self.manager.get_screen("home_screen").token = self.token


kv_loginscreen = """
<LoginScreen>:
    FloatLayout:
        id: l_screen
        Label:
            text: "Login"
            font_size: 48
            size_hint: .2, .4
            pos_hint:{'center_x':0.5, 'center_y':0.7}
        TextInput:
            id: login_email
            multiline: False
            write_tab: False
            hint_text: "Email"
            size_hint: .4, .05
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .55}
        TextInput:
            id: login_password
            multiline: False
            write_tab: False
            hint_text: "Password"
            font_size: 16
            size_hint: .4, .05
            pos_hint: {'center_x': .5, 'center_y': .45}
        Button:
            text: "Submit"
            font_size: 36
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .35, .1
            on_press: root.login()
            on_release:
                root.get_token()
                popup.open()
        Popup:
            id: popup
            on_parent: if self.parent == l_screen: l_screen.remove_widget(self)
            title: 'Successful login'
            content: popupcontent
            size_hint: .5, .5
            pos_hint: {'center_x': .5, 'center_y': .5}
            auto_dismiss: False
            Button:
                text: "Go to home"
                font_size: 24
                size_hint: .5, .3
                pos_hint: {'center_x': .5, 'center_y': .5}
                id: popupcontent
                text: 'Proceed to home'
                on_press:
                    root.go_to_home()
                    popup.dismiss()
        Label:
            font_size: 16
            size_hint: .4, .05
            pos_hint: {'center_x': .5, 'center_y': .22}
            text: 'Forgot password?'
"""
