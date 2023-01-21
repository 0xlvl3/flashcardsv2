from kivy.uix.screenmanager import Screen
from deck import user_deck


class CreateDeckScreen(Screen):
    def create(self):
        deck = self.manager.current_screen.ids.deck_to_create.text
        user_deck.create_deck(deck)
        self.manager.current_screen.ids.create_success.text = f"Your new deck {deck} is created! go back to the home screen and add flashcards!"

    def return_home(self):
        self.manager.current = "home_screen"

    def go_to_add_flashcard(self):
        self.manager.current = "add_flashcard_screen"
