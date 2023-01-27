from kivy.app import App
from kivy.uix.screenmanager import Screen
from flashcard import Flashcards
from fire_admin import db_system
import requests
import json

user_flashcards = Flashcards()


class AddFlashcardScreen(Screen):
    def update_text(self, widget_id, message):
        self.manager.current_screen.ids[widget_id].text = message

    def get_text(self, widget_id):
        return self.manager.current_screen.ids[widget_id].text

    def add_flashcard_to(self):
        """
        Function will take user input for a deck, then a question and answer
        to add to that specified deck.
        """
        deck = self.get_text("deck_to_add_card")
        user_question = self.get_text("add_question")
        user_answer = self.get_text("add_answer")
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
                    if user_question == k:
                        found = True
                        self.update_text(
                            "add_label",
                            f"{user_question} question exists in {deck} deck? Try adding another.",
                        )
                        self.update_text("add_question", "")
                        self.update_text("add_answer", "")
                        break
        if not found:
            try:
                user_flashcards.add_flashcards(deck, user_question, user_answer, uid)
                self.update_text(
                    "add_label",
                    f"{user_question} question added to {deck} deck! Add another?",
                )
                self.update_text("add_question", "")
                self.update_text("add_answer", "")

            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)["error"]
                if "Invalid data" in error:
                    self.update_text(
                        "add_label", "Please place data in all fields and try again."
                    )
                else:
                    self.update_text("add_label", error)

    def return_home(self):
        """
        Function will take user to home screen.
        """
        self.update_text("add_label", "Deck you wish to add card to.")
        self.update_text("deck_to_add_card", "")
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
            text: 'Deck you wish to add card to'
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
