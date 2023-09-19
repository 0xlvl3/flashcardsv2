# Kivy imports.
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Helper functions.
from helper import go_to_screen

# Constants.
from constants import (
    CREATE_DECK_SCREEN,
    ADD_FLASHCARD_SCREEN,
    INSPECT_DECK_SCREEN,
    PLAY_DECK_SCREEN,
    DELETE_DECK_SCREEN
)


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
        MDSwitch:
            pos_hint: {'center_x': .05, 'center_y': .05}
            width: dp(45)
            on_active: app.check(self, self.active)
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
        MDRaisedButton:
            text: "Create Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .7}
            size_hint: .35, .07
            on_press: root.go_to_create_deck()
        MDRaisedButton:
            text: "Add Flashcards"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint: .35, .07
            on_press: root.go_to_add_flashcard()
        MDRaisedButton:
            text: "Inspect Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .35, .07
            on_press: root.go_to_inspect_deck()
        MDRaisedButton:
            text: "Play Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint: .35, .07
            on_press: root.go_to_play()
        MDRaisedButton:
            text: "Delete Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .35, .07
            on_press: root.go_to_delete()
        MDRaisedButton:
            text: "Exit Application"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .1}
            size_hint: .35, .07
            on_press: app.stop()
"""

Builder.load_string(kv_homescreen)
