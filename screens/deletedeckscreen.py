from kivy.uix.screenmanager import Screen
from deck_module import user_deck
from helper import update_text
from helper import get_text
from helper import go_to_screen
from helper import get_token
from constants import HOME_SCREEN


class DeleteDeckScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deck = ""

    def load_deck(self):
        self.empty_check = get_text(self, "error")
        loaded_deck = get_text(self, "loaded_deck")
        if not loaded_deck:
            update_text(
                self,
                "error",
                "Please add a deck name to delete.",
            )
        else:
            self.deck = loaded_deck
            update_text(
                self,
                "confirm",
                f"Are you sure you want to delete {loaded_deck}?",
            )
            self.ids.popup.open()

    def confirm_delete_deck(self):
        # Will take loaded deck and delete in popup
        """
        Function will delete a specified user deck.
        """
        USER_TOKEN = get_token()
        user_deck.delete_deck(USER_TOKEN, self.deck)
        update_text(self, "loaded_deck", "")
        update_text(self, "error", f"{self.deck} deleted!")
        self.deck = ""

    def return_home(self):
        """
        Function will return user to the home screen.
        """
        update_text(self, "error", "")
        update_text(self, "loaded_deck", "")
        go_to_screen(self, HOME_SCREEN)


kv_deletedeckscreen = """
<DeleteDeckScreen>:
    FloatLayout:
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
        MDFillRoundFlatButton:
            text: "Delete"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint: .4, .1
            on_press: root.load_deck()
        MDFillRoundFlatButton:
            text: "Home"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint: .4, .1
            on_press: root.return_home()
        Popup:
            id: popup
            on_parent: if self.parent == d_screen: d_screen.remove_widget(self)
            title: 'Deck Player'
            content: popupcontent
            size_hint: .75, .75
            pos_hint: {'center_x': .5, 'center_y': .5}
            auto_dismiss: False
            FloatLayout:
                id:popupcontent
                Label:
                    id: confirm
                    text: 'Delete deck'
                    font_size: 24
                    pos_hint: {'center_x': .5, 'center_y': .8}
                    size_hint: .2, .2
                Button:
                    text: "Confirm"
                    font_size: 24
                    size_hint: .3, .15
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_press: root.confirm_delete_deck()
                    on_release: popup.dismiss()
                Button:
                    text: "X"
                    font_size: 20
                    size_hint: .05, .07
                    pos_hint: {'center_x': .975, 'center_y': .96}
                    on_press: popup.dismiss()
"""
