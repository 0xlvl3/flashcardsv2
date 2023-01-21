# Kivy / GUI.
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


# Modules.
from firebase import signup
from firebase import user_login
from deck import Deck
from flashcard import Flashcards

Builder.load_file("kv/frontend.kv")

# Global classes.
user_deck = Deck()
user_flashcards = Flashcards()


class StartScreen(Screen):
    def create_account(self):
        self.manager.current = "create_screen"

    def go_to_login(self):
        self.manager.current = "login_screen"


class CreateScreen(Screen):
    def create(self):
        email = self.manager.current_screen.ids.user_email.text
        password = self.manager.current_screen.ids.user_password.text
        signup(email, password)
        print("Account created")
        self.manager.current = "login_screen"


class LoginScreen(Screen):
    def login(self):
        print("Logging in")
        email = self.manager.current_screen.ids.login_email.text
        password = self.manager.current_screen.ids.login_password.text
        user_login(email, password)
        self.manager.current = "home_screen"


class HomeScreen(Screen):
    def switch_cards_screen(self):
        self.manager.current = "cards_screen"

    def create_deck_screen(self):
        self.manager.current = "create_deck_screen"

    def go_to_add_flashcard(self):
        self.manager.current = "add_flashcard_screen"

    def go_to_inspect_deck(self):
        self.manager.current = "inspect_deck_screen"

    def go_to_delete(self):
        self.manager.current = "delete_deck_screen"

    def go_to_play(self):
        self.manager.current = "play_deck_screen"


class CreateDeckScreen(Screen):
    def create(self):
        deck = self.manager.current_screen.ids.deck_to_create.text
        user_deck.create_deck(deck)
        self.manager.current_screen.ids.create_success.text = f"Your new deck {deck} is created! go back to the home screen and add flashcards!"

    def return_home(self):
        self.manager.current = "home_screen"

    def go_to_add_flashcard(self):
        self.manager.current = "add_flashcard_screen"


class AddFlashcardScreen(Screen):
    def add_flashcard_to(self):
        deck = self.manager.current_screen.ids.deck_to_add_card.text
        user_question = self.manager.current_screen.ids.add_question.text
        user_answer = self.manager.current_screen.ids.add_answer.text

        user_flashcards.add_flashcards(deck, user_question, user_answer)

        self.manager.current_screen.ids.add_label.text = (
            f"{user_question} question added to {deck} deck"
        )

    def return_home(self):
        self.manager.current = "home_screen"


class InspectDeckScreen(Screen):
    def index_cards(self):
        user_choice = self.manager.current_screen.ids.deck_to_inspect.text
        self.manager.current_screen.ids.load_deck.text = f"{user_choice} deck loaded"
        self.flashcards_indexed = user_deck.inspect_deck(user_choice)
        self.index = 0

    def show_next(self):
        if self.index < len(self.flashcards_indexed):
            card_index, question, answer = self.flashcards_indexed[self.index]
            self.manager.current_screen.ids.question.text = (
                f"{card_index} {question} {answer}"
            )
            self.index += 1
        else:
            self.manager.current_screen.ids.question.text = (
                "All flashcards have been shown"
            )

    def return_home(self):
        self.manager.current = "home_screen"


class DeleteDeckScreen(Screen):
    def gui_delete_deck(self):
        deck = self.manager.current_screen.ids.deck_to_delete.text
        user_deck.delete_deck(deck)

    def return_home(self):
        self.manager.current = "home_screen"


class PlayDeckScreen(Screen):
    def play(self):
        user_choice = self.manager.current_screen.ids.deck_to_play.text
        self.manager.current_screen.ids.deck_to_play.text = f"{user_choice} deck loaded"
        self.flashcards_indexed = user_deck.inspect_deck(user_choice)
        self.index = 0
        self.correct = 0
        self.incorrect = 0
        if self.index < len(self.flashcards_indexed):
            self.card_index, self.question, self.answer = self.flashcards_indexed[
                self.index
            ]
            self.manager.current_screen.ids.question.text = (
                f"{user_choice} loaded click go next card to start!"
            )
        else:
            self.manager.current_screen.ids.question.text = (
                "All flashcards have been shown"
            )

    def check_answer(self):
        user_answer = self.manager.current_screen.ids.answer.text
        if user_answer == self.answer:
            self.manager.current_screen.ids.after_answer.text = (
                f"Correct! answer was {self.answer}"
            )
            self.correct += 1
        else:
            self.manager.current_screen.ids.after_answer.text = (
                f"Incorrect the answer was: {self.answer}"
            )
            self.incorrect += 1

    def next_card(self):
        if self.index < len(self.flashcards_indexed):
            self.card_index, self.question, self.answer = self.flashcards_indexed[
                self.index
            ]
            self.manager.current_screen.ids.question.text = (
                f"{self.card_index}. Question: {self.question}"
            )
            self.manager.current_screen.ids.after_answer.text = f"What is the answer?"
            self.index += 1
        else:
            self.manager.current_screen.ids.question.text = f"""
All flashcards have been shown.
You got {self.correct} correct and {self.incorrect} incorrect.
Load another deck in the deck text input.
"""
            self.manager.current_screen.ids.after_answer.text = ""
            self.manager.current_screen.ids.deck_to_play.text = "Type deck to load here"

    def return_home(self):
        self.manager.current = "home_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
