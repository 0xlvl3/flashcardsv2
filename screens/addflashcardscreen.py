from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from flashcard_module import Flashcards
from fire_admin import db_system
from helper import get_text
from helper import update_text
from helper import go_to_screen
from helper import get_token
from constants import HOME_SCREEN
import requests
import json

user_flashcards = Flashcards()


class AddFlashcardScreen(Screen):
    def add_flashcard_to(self):
        """
        Function will take user input for a deck, then a question and answer
        to add to that specified deck.
        """

        deck = get_text(self, "deck_to_add_card")
        user_question = get_text(self, "add_question")
        user_answer = get_text(self, "add_answer")
        USER_TOKEN = get_token()

        # Block will check for empty deck value.

        if deck == "":
            update_text(
                self,
                "add_label",
                "No deck specified, add a existing deck and try again.",
            )

        # Block will check to see if user_question exists in deck specified.

        elif user_flashcards.check_for_existing_question(
            USER_TOKEN, deck, user_question
        ):
            update_text(
                self,
                "add_label",
                f"{user_question} question exists in {deck} deck? Try adding another.",
            )
            update_text(self, "add_question", "")
            update_text(self, "add_answer", "")

        # Block will run add_flashcard adding flashcard to specified deck
        else:
            message = user_flashcards.add_flashcard(
                deck, user_question, user_answer, USER_TOKEN
            )
            if message == "success":

                update_text(
                    self,
                    "add_label",
                    f"{user_question} question added to {deck} deck! Add another?",
                )
                update_text(self, "add_question", "")
                update_text(self, "add_answer", "")

            elif message == "Invalid data":
                update_text(
                    self,
                    "add_label",
                    "Please place data in all fields and try again.",
                )
            else:
                print("ll")

    def return_home(self):
        """
        Function will take user to home screen.
        """
        update_text(self, "add_label", "Deck you wish to add card to.")
        update_text(self, "deck_to_add_card", "")
        go_to_screen(self, "home_screen")


kv_addflashcardscreen = """
<AddFlashcardScreen>:
    FloatLayout:
        MDLabel:
            halign: 'center'
            text: 'Add Flashcards'
            font_size: 48
            pos_hint: {'center_x':.5, 'center_y':.85}
        MDLabel:
            halign: 'center'
            id: add_label
            text: 'Deck you wish to add card to'
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .75}
        MDTextField:
            mode: 'rectangle'
            multiline: False
            write_tab: False
            id: deck_to_add_card
            hint_text: "Deck name"
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .65}
            size_hint: .4, .11
        MDTextField:
            mode: 'rectangle'
            multiline: False
            write_tab: False
            id: add_question
            hint_text: "Question"
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .8, .11
        MDTextField:
            mode: 'rectangle'
            multiline: False
            write_tab: False
            id: add_answer
            hint_text: "Answer"
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint: .8, .11
        MDFillRoundFlatButton:
            text: "Home"
            pos_hint:{'center_x': .75, 'center_y': .2}
            font_size: 24
            size_hint: .4, 0.1
            on_press: root.return_home()
        MDFillRoundFlatButton:
            text: "Add flashcard"
            on_press: root.add_flashcard_to()
            pos_hint:{'center_x': .25, 'center_y': .2}
            font_size: 24
            size_hint: .4, 0.1
"""
