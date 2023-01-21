# Kivy / GUI.
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


# Modules.
from itertools import cycle
from firebase import signup
from firebase import user_login
from test_fb import db
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
    def inspect(self):
        deck = self.manager.current_screen.ids.deck_to_inspect.text

        ins = db.child(deck).child("flashcards").get()
        card_total = len(list(ins.val()))
        index = 0
        card_count = 0

        while index != card_total:
            start = list(ins.val().keys())[index]
            card_count += 1
            index += 1
            flashcards = ins.val()[start]
            for key, value in flashcards.items():
                self.manager.current_screen.ids.ins_question.text = (
                    f"Card:{card_count} Question: {key}"
                )
                self.manager.current_screen.ids.ins_answer.text = f"Answer: {value}"

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
        user_choice = self.manager.current_screen.ids.deck_play.text
        get_cards = db.child(user_choice).child("flashcards").get()
        card_total = len(list(get_cards.val()))
        index = 0
        card_counter = 0

        # Score counters.
        correct = 0
        incorrect = 0

        while index != card_total:
            start = list(get_cards.val().keys())[index]
            flashcards = get_cards.val()[start]

            # Iterate
            card_counter += 1
            index += 1

            for key, value in flashcards.items():
                self.questions = cycle(
                    [f"{card_counter}. {key} {value}" for i in range(index, card_total)]
                )

    def next_answer(self):
        self.text = next(self.questions)

    def return_home(self):
        self.manager.current = "home_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
