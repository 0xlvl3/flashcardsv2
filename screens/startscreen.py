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

        Label:
            text: "kv Flashcards"
            font_size: 48
            size_hint: .2, .4
            pos_hint:{'center_x':0.5, 'center_y':0.6}
        Button:
            on_press: root.create_account()
            text: "Create Account"
            font_size: 24
            size_hint: .35, .1
		    pos_hint: {'center_x': .5, 'center_y': .45}
        Button:
            on_press: root.go_to_login()
            text: "Login"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .35, .1
"""
