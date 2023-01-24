from kivy.app import App
from kivy.uix.screenmanager import Screen
from deck import user_deck


class DeleteDeckScreen(Screen):
    def gui_delete_deck(self):
        """
        Function will delete a specified user deck.
        """
        deck = self.manager.current_screen.ids.deck_to_delete.text
        token = App.get_running_app().logged_token
        user_deck.delete_deck(token, deck)

    def return_home(self):
        """
        Function will return user to the home screen.
        """
        self.manager.current = "home_screen"


kv_deletedeckscreen = """
<DeleteDeckScreen>:
	GridLayout:
		cols: 1 
		Label:
			text: 'Delete deck'
		TextInput:
			multiline: False
			write_tab: False
			id: deck_to_delete
			text: 'Choose which deck you want to delete'
		GridLayout:
			cols: 2 
			Button:
				text: 'Delete deck'
				on_press: root.gui_delete_deck()
			Button:
				text: 'Go to home screen'
				on_press: root.return_home()
"""
