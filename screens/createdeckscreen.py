from kivy.app import App
from kivy.uix.screenmanager import Screen
from deck import user_deck
from fire_admin import db_system


class CreateDeckScreen(Screen):
    def update_text(self, widget_id, message):
        self.manager.current_screen.ids[widget_id].text = message

    def get_text(self, widget_id):
        return self.manager.current_screen.ids[widget_id].text

    def create(self):
        """
        Function will take user input and create a deck.
        """
        _token = App.get_running_app().logged_token

        # Will check for empty value.
        # Bug if there is no value and user creates it will clear all decks.

        deck = self.get_text("deck_to_create")
        if deck == "":
            self.update_text("create_success", "Try again no deck was specified")
        else:
            try:
                # This block will check to see if deck already exists.

                print(_token)
                deck_check = db_system.child(_token).get()
                data = deck_check.val()
                keys = list(data.keys())
                found = False
                for key in keys:
                    if deck == key:
                        found = True
                        print(key)
                        self.update_text("create_success", f"{deck} already exists!")
                        self.update_text("deck_to_create", "")
                        break

                    # Block will create deck.

                if not found:
                    user_deck.create_deck(_token, deck)
                    self.update_text(
                        "create_success",
                        f"{_token} Your new deck {deck} is created! go back to the home screen and add flashcards!",
                    )
                    self.update_text("deck_to_create", "")
            except Exception as e:
                print(e)

    def return_home(self):
        """
        Function will take user to home screen.
        """
        self.update_text("create_success", "")
        self.manager.current = "home_screen"

    def go_to_add_flashcard(self):
        """
        Function will take user to add flashcard screen.
        """
        self.update_text("create_success", "")
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
