from kivy.app import App
from kivy.uix.screenmanager import Screen
from deck import user_deck


class CreateDeckScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def create(self):
        """
        Function will take user input and create a deck.
        """
        _token = App.get_running_app().logged_token

        deck = self.manager.current_screen.ids.deck_to_create.text
        user_deck.create_deck(_token, deck)
        self.manager.current_screen.ids.create_success.text = f"{_token} Your new deck {deck} is created! go back to the home screen and add flashcards!"

    def return_home(self):
        """
        Function will take user to home screen.
        """
        self.manager.current = "home_screen"

    def go_to_add_flashcard(self):
        """
        Function will take user to add flashcard screen.
        """
        self.manager.current = "add_flashcard_screen"
