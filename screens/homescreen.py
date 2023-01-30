# Kivy imports.
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Helper functions.
from helper import go_to_screen

# Constants.
from constants import CREATE_DECK_SCREEN
from constants import ADD_FLASHCARD_SCREEN
from constants import INSPECT_DECK_SCREEN
from constants import PLAY_DECK_SCREEN
from constants import DELETE_DECK_SCREEN


class HomeScreen(MDScreen):
    """
    HomeScreen will be used to navigate the user.
    """

    def go_to_create_deck(self):
        """
        Function will take user to create deck screen.
        """
        go_to_screen(self, CREATE_DECK_SCREEN)

    def go_to_add_flashcard(self):
        """
        Function will take user to add flashcard screen.
        """
        go_to_screen(self, ADD_FLASHCARD_SCREEN)

    def go_to_inspect_deck(self):
        """
        Function will take user to inspect deck screen.
        """
        go_to_screen(self, INSPECT_DECK_SCREEN)

    def go_to_delete(self):
        """
        Function will take user to delete deck screen.
        """
        go_to_screen(self, DELETE_DECK_SCREEN)

    def go_to_play(self):
        """
        Function will take user to play deck screen.
        """
        go_to_screen(self, PLAY_DECK_SCREEN)


kv_homescreen = """
<HomeScreen>:
    MDFloatLayout:
        MDLabel:
            text: 'Welcome User'
            halign: 'center'
            font_size: 28
            pos_hint: {'center_x':.5, 'center_y':.85}
        MDLabel:
            text: 'Select an option below'
            font_size: 16
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': .8}
        MDFillRoundFlatButton:
            text: "Create Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .7}
            size_hint: .35, .07
            on_press: root.go_to_create_deck()
        MDFillRoundFlatButton:
            text: "Add Flashcards"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint: .35, .07
            on_press: root.go_to_add_flashcard()
        MDFillRoundFlatButton:
            text: "Inspect Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .35, .07
            on_press: root.go_to_inspect_deck()
        MDFillRoundFlatButton:
            text: "Play Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint: .35, .07
            on_press: root.go_to_play()
        MDFillRoundFlatButton:
            text: "Delete Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .35, .07
            on_press: root.go_to_delete()
        MDFillRoundFlatButton:
            text: "Exit Application"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .1}
            size_hint: .35, .07
            on_press: app.stop()
"""

Builder.load_string(kv_homescreen)
