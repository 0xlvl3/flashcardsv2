from kivy.uix.screenmanager import Screen
from deck import user_deck


class DeleteDeckScreen(Screen):
    def gui_delete_deck(self):
        deck = self.manager.current_screen.ids.deck_to_delete.text
        user_deck.delete_deck(deck)

    def return_home(self):
        self.manager.current = "home_screen"
