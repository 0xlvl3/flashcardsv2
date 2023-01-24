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
