# Kivy / GUI.
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


# Modules.
from firebase import signup
from firebase import user_login
from test_fb import db
from deck import Deck
from flashcard import Flashcards

Builder.load_file("frontend.kv")

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


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
