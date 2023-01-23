from kivy.uix.screenmanager import Screen
from deck import user_deck
from tkm import TokenManager


class CreateDeckScreen(Screen):
    def create(self):
        """
        Function will take user input and create a deck.
        """
        token = TokenManager.get_token()
        deck = self.manager.current_screen.ids.deck_to_create.text
        user_deck.create_deck(user=token, deck=deck)
        self.manager.current_screen.ids.create_success.text = f"Your new deck {deck} is created! go back to the home screen and add flashcards!"

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
