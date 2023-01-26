from kivy.app import App
from kivy.uix.screenmanager import Screen
from flashcard import Flashcards
from fire_admin import db_system

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
        found = False

        # Question check for dub questions.

        deck_check = db_system.child(uid).child(deck).child("flashcards").get()
        data = deck_check.val()
        if data is None:
            pass
        else:
            pair = list(data.items())
            for key, value in pair:
                for k, v in value.items():
                    if user_question in k:
                        found = True
                        self.manager.current_screen.ids.add_label.text = f"{user_question} question exists in {deck} deck? Try adding another."
                        self.manager.current_screen.ids.add_question.text = ""
                        self.manager.current_screen.ids.add_answer.text = ""
                        break
        if not found:
            user_flashcards.add_flashcards(deck, user_question, user_answer, uid)
            self.manager.current_screen.ids.add_label.text = (
                f"{user_question} question added to {deck} deck! Add another?"
            )
            self.manager.current_screen.ids.add_question.text = ""
            self.manager.current_screen.ids.add_answer.text = ""

    def return_home(self):
        """
        Function will take user to home screen.
        """
        self.manager.current = "home_screen"


kv_addflashcardscreen = """
<AddFlashcardScreen>:
    FloatLayout:
        Label:
            text: 'Add Flashcards'
            font_size: 28
            pos_hint: {'center_x':.5, 'center_y':.8}
        Label:
            id: add_label
            text: 'Deck you want to add card'
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .7}
        TextInput:
            multiline: False
            write_tab: False
            id: deck_to_add_card
            hint_text: "Deck name"
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .65}
            size_hint: .4, .05
        TextInput:
            multiline: False
            write_tab: False
            id: add_question
            hint_text: "Question"
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .8, .05
        TextInput:
            multiline: False
            write_tab: False
            id: add_answer
            hint_text: "Answer"
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint: .8, .05
        Button:
            text: "Home"
            pos_hint:{'center_x': .75, 'center_y': .2}
            font_size: 20
            size_hint: .4, 0.1
            on_press: root.return_home()
        Button:
            text: "Add flashcard"
            on_press: root.add_flashcard_to()
            pos_hint:{'center_x': .25, 'center_y': .2}
            font_size: 20
            size_hint: .4, 0.1
"""
