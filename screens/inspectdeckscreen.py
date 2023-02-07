# Kivy imports.
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock

# Module imports.
from deck_module import user_deck

# Helper functions.
from helper import (
    get_text,
    update_text,
    go_to_screen,
    get_token
)

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

        # If no input in field from user on submit this block runs.

        if not user_choice:
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
                self.inspect_index = 0

                self.ids.popup.open()
            except Exception as e:  # it is very risky to catch exceptions like that
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
                "All flashcards have been shown. Resetting please wait.",
            )
            Clock.schedule_once(self.reset_flashcards, 2)

    def reset_flashcards(self, time):
        """
        Function is used at the end of card loop, placed in Clock callback will dismiss window when done.
        """
        update_text(self, "deck_to_inspect", "")
        update_text(self, "error", "")
        self.ids.popup.dismiss()

    def return_home(self):
        """
        Function will return the user back to the home screen.
        """
        update_text(self, "error", "")
        go_to_screen(self, HOME_SCREEN)


kv_inspectdeckscreen = """
<InspectDeckScreen>:
    MDFloatLayout:
        id: ins_screen
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
        Popup:
            id: popup
            on_parent: if self.parent == ins_screen: ins_screen.remove_widget(self)
            title: 'Deck Inspector'
            content: popupcontent
            size_hint: .7, .7
            pos_hint: {'center_x': .5, 'center_y': .5}
            auto_dismiss: False
            FloatLayout:
                id:popupcontent
                Label:
                    text: 'Deck loaded! click next to see first card'
                    id: question
                    font_size: 18
                    pos_hint: {'center_x': .5, 'center_y': .7}
                    size_hint: .2, .2
                MDRaisedButton:
                    text: "Go next"
                    font_size: 24
                    size_hint: .5, .2
                    pos_hint: {'center_x': .5, 'center_y': .4}
                    on_press: root.show_next()
                MDRaisedButton:
                    text: "X"
                    font_size: 18
                    size_hint: .05, .05
                    pos_hint: {'center_x': .945, 'center_y': .94}
                    on_press: popup.dismiss()
"""


Builder.load_string(kv_inspectdeckscreen)
