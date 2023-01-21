from kivy.uix.screenmanager import Screen
from deck import user_deck


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
