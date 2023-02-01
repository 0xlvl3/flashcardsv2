# Kivy imports.
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# Modules.
from flashcard_module import Flashcards

# Helper functions.
from helper import get_text
from helper import update_text
from helper import go_to_screen
from helper import get_token

# Constants.
from constants import HOME_SCREEN


class AddFlashcardScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.user_flashcards = Flashcards()

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
                "error",
                "No deck specified, add a existing deck and try again.",
            )

        # Block will check to see if user_question exists in deck specified.

        elif self.user_flashcards.check_for_existing_question(
            USER_TOKEN, deck, user_question
        ):
            update_text(
                self,
                "error",
                f"{user_question} question exists in {deck} deck. Try adding another?",
            )
            update_text(self, "add_question", "")
            update_text(self, "add_answer", "")

        # Block will run add_flashcard adding flashcard to specified deck
        else:
            message = self.user_flashcards.add_flashcard(
                deck, user_question, user_answer, USER_TOKEN
            )

            # Block will add flashcard if success.

            if message == "success":

                update_text(
                    self,
                    "error",
                    f"{user_question} question added to {deck} deck! Add another?",
                )
                update_text(self, "add_question", "")
                update_text(self, "add_answer", "")

            # Block will throw error for invalid data.

            elif message == "Invalid data":
                update_text(
                    self,
                    "error",
                    "Please place data in all fields and try again.",
                )

            # If error is not known it will print to error.

            else:
                update_text(self, "error", message)

    def return_home(self):
        """
        Function will take user to home screen.
        """
        update_text(self, "error", "Deck you wish to add card to.")
        update_text(self, "deck_to_add_card", "")
        go_to_screen(self, HOME_SCREEN)


kv_addflashcardscreen = """
<AddFlashcardScreen>:
    MDFloatLayout:
        MDLabel:
            halign: 'center'
            text: 'Add Flashcards'
            font_size: 48
            pos_hint: {'center_x':.5, 'center_y':.85}
        MDLabel:
            halign: 'center'
            id: error
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
        MDRaisedButton:
            text: "Home"
            pos_hint:{'center_x': .75, 'center_y': .2}
            font_size: 24
            size_hint: .4, 0.1
            on_press: root.return_home()
        MDRaisedButton:
            text: "Add flashcard"
            on_press: root.add_flashcard_to()
            pos_hint:{'center_x': .25, 'center_y': .2}
            font_size: 24
            size_hint: .4, 0.1
"""


Builder.load_string(kv_addflashcardscreen)
