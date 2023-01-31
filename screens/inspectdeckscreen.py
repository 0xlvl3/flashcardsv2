# Kivy imports.
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

# Module imports.
from deck_module import user_deck

# Helper functions.
from helper import get_text
from helper import update_text
from helper import go_to_screen
from helper import get_token

# Constants.
from constants import HOME_SCREEN


class InspectDeckScreen(MDScreen):
    def index_cards(self):
        """
        Function will load user specified deck, deck will be saved to
        an index that will be iterated over.
        """
        user_choice = get_text(self, "deck_to_inspect")
        USER_TOKEN = get_token()

        # Inspector Popup.
        self.dialog = MDDialog(
            auto_dismiss=False, title="Success", id="question", text=""
        )

        # If no input in field from user on submit this block runs.

        if user_choice == "":
            update_text(
                self, "error", "Text field is empty, please enter a deck and try again."
            )

        # Input exists it will run the try block.

        else:

            # Block will index cards if deck exists. Then open the inspect deck window.
            # If deck doesn't exist it will error.

            try:
                self.flashcards_indexed = user_deck.inspect_deck(
                    USER_TOKEN, user_choice
                )

                print(self.flashcards_indexed)

                self.inspect_index = 0
                print(self.inspect_index)

                print(self.dialog.open())
                self.dialog.open()

            except Exception as e:
                update_text(self, "deck_to_inspect", "")
                e = f"Deck doesn't exist: {user_choice}"
                update_text(self, "error", e)

    def show_next(self):
        """
        Function will be used to iterate over our indexed flashcards through
        the next button.
        """
        if self.inspect_index < len(self.flashcards_indexed):
            card_index, question, answer = self.flashcards_indexed[self.inspect_index]
            update_text(self, "question", f"{card_index} {question} {answer}")
            self.inspect_index += 1
        else:
            update_text(
                self,
                "question",
                "All flashcards have been shown. Click button to exit.",
            )

    def return_home(self):
        """
        Function will return the user back to the home screen.
        """
        update_text(self, "error", "")
        go_to_screen(self, HOME_SCREEN)


kv_inspectdeckscreen = """
<InspectDeckScreen>:
    MDFloatLayout:
        MDLabel:
            text: 'Deck Inspector'
            font_size: 48
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': .8}
        MDLabel:
            text: ''
            id: error
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .6}
            halign: 'center'
        MDTextField:
            mode: 'rectangle'
            multiline: False
            write_tab: False
            front_size: 18
            id: deck_to_inspect
            hint_text: 'Deck name'
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .4, .11
        MDRaisedButton:
            text: "Load deck"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .35, .1
            on_press: root.index_cards()
        MDRaisedButton:
            text: "Home"
            pos_hint:{'center_x': .5, 'center_y': .15}
            font_size: 24
            size_hint: .35, .1
            on_press: root.return_home()
"""


Builder.load_string(kv_inspectdeckscreen)
