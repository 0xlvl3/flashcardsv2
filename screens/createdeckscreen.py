from kivy.app import App
from kivy.uix.screenmanager import Screen
from deck import user_deck


class CreateDeckScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def create(self):
        """
        Function will take user input and create a deck.
        """
        _token = App.get_running_app().logged_token

        # Will check for empty value.
        # Bug if there is no value and user creates it will clear all decks.
        deck = self.manager.current_screen.ids.deck_to_create.text
        if deck == "":
            self.manager.current_screen.ids.create_success.text = (
                "Try again no deck was specified"
            )
        else:
            try:
                user_deck.create_deck(_token, deck)
                self.manager.current_screen.ids.create_success.text = f"{_token} Your new deck {deck} is created! go back to the home screen and add flashcards!"
            except Exception as e:
                print(e)

    def return_home(self):
        """
        Function will take user to home screen.
        """
        self.manager.current = "home_screen"

    def go_to_add_flashcard(self):
        """
        Function will take user to add flashcard screen.
        """
        self.manager.current = "add_flashcard_screen"


kv_createdeckscreen = """
<CreateDeckScreen>:
    FloatLayout:
        Label:
            text: 'Create a Deck'
            font_size: 28
            pos_hint: {'center_x':.5, 'center_y':.7}
        Label:
            text: 'Name your deck'
            id: create_success
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .55}
        TextInput:
            hint_text: "Deck name"
            id: deck_to_create
			multiline: False
			write_tab: False
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .4, .05
        Button:
            text: "Create"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint: .4, .1
            on_press: root.create()
        Button:
            text: "Home"
            pos_hint:{'center_x': .75, 'center_y': .2}
            font_size: 20
            size_hint: .4, 0.1
            on_press: root.return_home()
        Button:
            text: "Add flashcards"
            pos_hint:{'center_x': .25, 'center_y': .2}
            font_size: 20
            size_hint: .4, 0.1
            on_press: root.go_to_add_flashcard()

"""
