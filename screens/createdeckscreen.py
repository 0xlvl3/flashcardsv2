# Kivy imports.
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# Module imports.
from deck_module import user_deck

# Helper functions.
from helper import update_text
from helper import get_text
from helper import go_to_screen

# Constants.
from constants import HOME_SCREEN
from constants import ADD_FLASHCARD_SCREEN


class CreateDeckScreen(MDScreen):
    def create(self):
        """
        Function will take user input and create a deck.
        """
        USER_TOKEN = MDApp.get_running_app().TOKEN

        # Will check for empty value.
        # Bug if there is no value and user creates it will clear all decks.

        deck = get_text(self, "deck_to_create")

        if deck == "":
            update_text(self, "create_success", "Try again no deck was specified")

        # We check if deck is known.

        elif user_deck.check_for_known_deck(USER_TOKEN, deck):
            update_text(self, "create_success", f"{deck} already exists!")
            update_text(self, "deck_to_create", "")

        # Else block will create deck.

        else:
            user_deck.create_deck(USER_TOKEN, deck)
            update_text(
                self,
                "create_success",
                f"{USER_TOKEN} Your new deck {deck} is created! go back to the home screen and add flashcards!",
            )
            update_text(self, "deck_to_create", "")

    def return_home(self):
        """
        Function will take user to home screen.
        """
        update_text(self, "create_success", "")
        go_to_screen(self, HOME_SCREEN)

    def go_to_add_flashcard(self):
        """
        Function will take user to add flashcard screen.
        """
        update_text(self, "create_success", "")
        go_to_screen(self, ADD_FLASHCARD_SCREEN)


kv_createdeckscreen = """
<CreateDeckScreen>:
    MDFloatLayout:
        MDLabel:
            text: 'Create a Deck'
            halign: 'center'
            font_size: 48
            pos_hint: {'center_x':.5, 'center_y':.7}
        MDLabel:
            halign: 'center'
            text: ''
            id: create_success
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .6}
        MDTextField:
            mode: 'rectangle'
            hint_text: "Deck name"
            id: deck_to_create
			multiline: False
			write_tab: False
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .4, .11
        MDRaisedButton:
            text: "Create"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint: .4, .1
            on_press: root.create()
        MDRaisedButton:
            text: "Home"
            pos_hint:{'center_x': .75, 'center_y': .2}
            font_size: 24
            size_hint: .4, 0.1
            on_press: root.return_home()
        MDRaisedButton:
            text: "Add flashcards"
            pos_hint:{'center_x': .25, 'center_y': .2}
            font_size: 24
            size_hint: .4, 0.1
            on_press: root.go_to_add_flashcard()

"""


Builder.load_string(kv_createdeckscreen)
