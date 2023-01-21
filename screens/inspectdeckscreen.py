from kivy.uix.screenmanager import Screen
from deck import user_deck


class InspectDeckScreen(Screen):
    def index_cards(self):
        user_choice = self.manager.current_screen.ids.deck_to_inspect.text
        self.manager.current_screen.ids.load_deck.text = f"{user_choice} deck loaded"
        self.flashcards_indexed = user_deck.inspect_deck(user_choice)
        self.ins_index = 0

    def show_next(self):
        if self.ins_index < len(self.flashcards_indexed):
            card_index, question, answer = self.flashcards_indexed[self.ins_index]
            self.manager.current_screen.ids.question.text = (
                f"{card_index} {question} {answer}"
            )
            self.ins_index += 1
        else:
            self.manager.current_screen.ids.question.text = (
                "All flashcards have been shown"
            )

    def return_home(self):
        self.manager.current = "home_screen"
