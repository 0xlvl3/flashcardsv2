from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


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
<StartScreen>:
	GridLayout:
		spacing: 30
		padding: 
		cols: 1
		Label:
			font_size: 32
			text: 'Start Screen'
		
		# Startscreen Buttons.
		GridLayout:
			cols: 2
			size_hint_y: 0.45
			spacing: 30 
			padding: 20
			Button:
				text: 'Create an account'
				on_press: root.create_account()
			Button:
				text: 'Have an account, go to login'
				on_press: root.go_to_login()
"""

Builder.load_string(kv_startscreen)
