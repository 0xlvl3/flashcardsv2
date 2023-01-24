from kivy.uix.screenmanager import Screen
from kivy.app import App
from deck import user_deck


class InspectDeckScreen(Screen):
    def index_cards(self):
        """
        Function will load user specified deck, deck will be saved to
        an index that will be iterated over.
        """
        user_choice = self.manager.current_screen.ids.deck_to_inspect.text
        token = App.get_running_app().logged_token
        self.manager.current_screen.ids.load_deck.text = f"{user_choice} deck loaded"
        self.flashcards_indexed = user_deck.inspect_deck(token, user_choice)
        self.ins_index = 0

    def show_next(self):
        """
        Function will be used to iterate over our indexed flashcards through
        a button. When we press button we iterate bringing the next flashcard up.
        """
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
        """
        Function will return the user back to the home screen.
        """
        self.manager.current = "home_screen"


kv_inspectdeckscreen = """
<InspectDeckScreen>:
	GridLayout:
		cols: 1
		Label:
			id: question
			text: 'Which deck will you inspect?'
		TextInput:
			multiline: False
			write_tab: False
			id: deck_to_inspect
			text: 'Deck name'
		GridLayout:
			cols: 2 
			Button:
				id: load_deck
				text: 'Load deck'
				on_press: root.index_cards()
			Button:
				text: "Back to home"
				on_press: root.return_home()
			Button:
				text: "Go next card"
				on_press: root.show_next()
"""
