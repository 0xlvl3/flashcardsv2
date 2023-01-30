from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder


class StartScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        app = MDApp.get_running_app()
        self.theme = app.theme_cls.theme_style

    def set_btn_color(self):
        if self.theme == "Light":
            return [1, 0, 0, 1]
        else:
            return [0, 1, 0, 1]

    def create_account(self):
        """
        Function take user to create account screen.
        """

        print(self.theme)
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
            pos_hint: {'center_x': .05, 'center_y': .05}
            width: dp(45)
            on_active: app.check(self, self.active)
        MDLabel:
            id: heading
            text: "kv Flashcards"
            halign: 'center'
            font_size: 56
            pos_hint:{'center_x': .5, 'center_y': .65}
        MDFillRoundFlatButton:
            on_press: root.create_account()
            md_bg_color: root.set_btn_color()
            text_color: [0, 0, 0, 1]
            id: 'create_btn'
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

Builder.load_string(kv_startscreen)
