from kivy.app import App
from kivy.uix.screenmanager import Screen
from deck import user_deck


class DeleteDeckScreen(Screen):
    def load_deck(self):
        loaded_deck = self.manager.current_screen.ids.loaded_deck.text
        self.manager.current_screen.ids.confirm.text = (
            f"Are you sure you want to delete {loaded_deck}?"
        )
        self.deck = loaded_deck

    def gui_delete_deck(self):
        # Will take loaded deck and delete in popup
        """
        Function will delete a specified user deck.
        """
        token = App.get_running_app().logged_token
        user_deck.delete_deck(token, self.deck)
        self.manager.current_screen.ids.loaded_deck.text = ""

    def return_home(self):
        """
        Function will return user to the home screen.
        """
        self.manager.current = "home_screen"


kv_deletedeckscreen = """
<DeleteDeckScreen>:
    FloatLayout:
        id: d_screen
        Label:
            text: "Delete Deck"
            font_size: 32
            pos_hint: {'center_x': .5, 'center_y': .7}
            size_hint: .35, .1
        TextInput:
            id: loaded_deck
            hint_text: "Deck to Delete"
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .4, .1
        Button:
            text: "Delete"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint: .35, .1
            on_press: root.load_deck()
            on_release: popup.open()
        Button:
            text: "Home"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint: .35, .1
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
                    on_press: root.gui_delete_deck()
                    on_release: popup.dismiss()
                Button:
                    text: "X"
                    font_size: 20
                    size_hint: .05, .07
                    pos_hint: {'center_x': .975, 'center_y': .96}
                    on_press: popup.dismiss()
"""
