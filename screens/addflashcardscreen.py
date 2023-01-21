from kivy.uix.screenmanager import Screen
from flashcard import Flashcards

user_flashcards = Flashcards()


class AddFlashcardScreen(Screen):
    def add_flashcard_to(self):
        """
        Function will take user input for a deck, then a question and answer
        to add to that specified deck.
        """
        deck = self.manager.current_screen.ids.deck_to_add_card.text
        user_question = self.manager.current_screen.ids.add_question.text
        user_answer = self.manager.current_screen.ids.add_answer.text

        user_flashcards.add_flashcards(deck, user_question, user_answer)

        self.manager.current_screen.ids.add_label.text = (
            f"{user_question} question added to {deck} deck"
        )

    def return_home(self):
        """
        Function will take user to home screen.
        """
        self.manager.current = "home_screen"
