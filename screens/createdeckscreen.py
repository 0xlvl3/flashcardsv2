from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from deck import user_deck
from fire_admin import db_system
from helper import update_text
from helper import get_text
from helper import go_to_screen
from constants import HOME_SCREEN
from constants import ADD_FLASHCARD_SCREEN


class CreateDeckScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

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
        else:
            try:
                # This block will check to see if deck already exists.

                print(USER_TOKEN)
                deck_check = db_system.child(USER_TOKEN).get()
                data = deck_check.val()
                keys = list(data.keys())
                found = False
                for key in keys:
                    if deck == key:
                        found = True
                        print(key)
                        update_text(self, "create_success", f"{deck} already exists!")
                        update_text(self, "deck_to_create", "")
                        break

                    # Block will create deck.

                if not found:
                    user_deck.create_deck(USER_TOKEN, deck)
                    update_text(
                        self,
                        "create_success",
                        f"{USER_TOKEN} Your new deck {deck} is created! go back to the home screen and add flashcards!",
                    )
                    update_text(self, "deck_to_create", "")
            except Exception as e:
                print(e)

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
    FloatLayout:
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
        MDFillRoundFlatButton:
            text: "Create"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint: .4, .1
            on_press: root.create()
        MDFillRoundFlatButton:
            text: "Home"
            pos_hint:{'center_x': .75, 'center_y': .2}
            font_size: 24
            size_hint: .4, 0.1
            on_press: root.return_home()
        MDFillRoundFlatButton:
            text: "Add flashcards"
            pos_hint:{'center_x': .25, 'center_y': .2}
            font_size: 24
            size_hint: .4, 0.1
            on_press: root.go_to_add_flashcard()

"""
