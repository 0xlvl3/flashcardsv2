from kivy.app import App
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
        uid = App.get_running_app().logged_token

        user_flashcards.add_flashcards(deck, user_question, user_answer, uid)

        self.manager.current_screen.ids.add_label.text = (
            f"{user_question} question added to {deck} deck"
        )

    def return_home(self):
        """
        Function will take user to home screen.
        """
        self.manager.current = "home_screen"


kv_addflashcardscreen = """
<AddFlashcardScreen>:
	GridLayout:
		cols: 1 
		Label:
			text: 'Add flashcards here'
			id: add_label
		TextInput:
			multiline: False
			write_tab: False
			id: deck_to_add_card
			text: "Deck to add card"
		TextInput:
			multiline: False
			write_tab: False
			id: add_question
			text: "Question for your flashcard"
		TextInput:
			multiline: False
			write_tab: False
			id: add_answer
			text: "Answer for that flashcard"
		GridLayout:
			cols: 2 
			Button:
				text: 'Add flashcard'
				on_press: root.add_flashcard_to()
			Button:
				text: "Go back to home"
				on_press: root.return_home()
"""
