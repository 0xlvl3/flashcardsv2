# Kivy imports.
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

# Module imports.
from deck_module import user_deck

# Helper functions.
from helper import update_text
from helper import get_text
from helper import go_to_screen
from helper import get_token

# Constants.
from constants import HOME_SCREEN


class DeleteDeckScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.dialog = None
        self.deck = ""

    # Dialog confirmation window for deletion.

    def confirm_window(self):
        if not self.dialog:
            self.dialog = MDDialog(
                auto_dismiss=False,
                title="Confirmation window",
                text="This deck will not be recoverable, click confirm to delete, cancel to exit.",
                buttons=[
                    MDRaisedButton(
                        text="Confirm",
                        on_press=self.confirm_delete_deck,
                        on_release=self.close_dialog,
                    ),
                    MDRaisedButton(
                        text="Cancel",
                        on_press=self.close_dialog,
                    ),
                ],
            )
        self.dialog.open()

    # Will load the deck.

    def load_deck(self):
        self.empty_check = get_text(self, "error")
        loaded_deck = get_text(self, "loaded_deck")
        if not loaded_deck:
            update_text(
                self,
                "error",
                "Please add a deck name to delete.",
            )
        if loaded_deck:
            self.deck = loaded_deck

    def confirm_delete_deck(self, *args):
        # Will take loaded deck and delete in popup
        """
        Function will delete a specified user deck.
        """
        USER_TOKEN = get_token()
        user_deck.delete_deck(USER_TOKEN, self.deck)
        update_text(self, "loaded_deck", "")
        update_text(self, "error", f"{self.deck} deleted!")
        self.deck = ""

    # Will close the confirmation dialog.

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def return_home(self):
        """
        Function will return user to the home screen.
        """
        update_text(self, "error", "")
        update_text(self, "loaded_deck", "")
        go_to_screen(self, HOME_SCREEN)


kv_deletedeckscreen = """
<DeleteDeckScreen>:
    MDFloatLayout:
        id: d_screen
        MDLabel:
            text: "Delete Deck"
            font_size: 48
            pos_hint: {'center_x': .5, 'center_y': .75}
            halign: 'center'
        MDLabel:
            text: "Please add a deck name to delete."
            id: error
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .6}
            halign: 'center'
        MDTextField:
            mode: 'rectangle'
            id: loaded_deck
            hint_text: "Deck to Delete"
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .4, .11
        MDRaisedButton:
            text: "Delete"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint: .4, .1
            on_press:
                root.load_deck()
                root.confirm_window()
        MDRaisedButton:
            text: "Home"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint: .4, .1
            on_press: root.return_home()
"""
Builder.load_string(kv_deletedeckscreen)
