from kivy.uix.screenmanager import Screen


class StartScreen(Screen):
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
        MDSwitch:
            pos_hint: {'center_x': .1, 'center_y': .9}
            width: dp(45)
            on_active: app.check(*args)
        MDLabel:
            id: heading
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
