from kivy.uix.screenmanager import Screen
from kivy.app import App
from deck import user_deck


class InspectDeckScreen(Screen):
    def index_cards(self):
        """
        Function will load user specified deck, deck will be saved to
        an index that will be iterated over.
        """
        user_choice = self.manager.current_screen.ids.deck_to_inspect.text
        token = App.get_running_app().logged_token
        # self.manager.current_screen.ids.load_deck.text = f"{user_choice} deck loaded"
        self.flashcards_indexed = user_deck.inspect_deck(token, user_choice)
        self.ins_index = 0

    def show_next(self):
        """
        Function will be used to iterate over our indexed flashcards through
        a button. When we press button we iterate bringing the next flashcard up.
        """
        if self.ins_index < len(self.flashcards_indexed):
            card_index, question, answer = self.flashcards_indexed[self.ins_index]
            self.manager.current_screen.ids.question.text = (
                f"{card_index} {question} {answer}"
            )
            self.ins_index += 1
        else:
            self.manager.current_screen.ids.question.text = (
                "All flashcards have been shown"
            )
            self.manager.current_screen.ids.deck_to_inspect.text = ""

    def return_home(self):
        """
        Function will return the user back to the home screen.
        """
        self.manager.current = "home_screen"


kv_inspectdeckscreen = """
<InspectDeckScreen>:
    FloatLayout:
        id: ins_screen
        Label:
            text: 'Deck Inspector'
            font_size: 32
            pos_hint: {'center_x': .5, 'center_y': .7}
        TextInput:
            multiline: False
            write_tab: False
            id: deck_to_inspect
            hint_text: 'Deck name'
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .4, .05
        Button:
            text: "Load deck"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint: .35, .1
            on_press: root.index_cards()
            on_release: popup.open()
        Button:
            text: "Home"
            pos_hint:{'center_x': .5, 'center_y': .2}
            font_size: 24
            size_hint: .35, .1
            on_press: root.return_home()
        Popup:
            id: popup
            on_parent: if self.parent == ins_screen: ins_screen.remove_widget(self)
            title: 'Deck Inspector'
            content: popupcontent
            size_hint: .5, .5
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
                Button:
                    text: "Go next"
                    font_size: 24
                    size_hint: .5, .2
                    pos_hint: {'center_x': .5, 'center_y': .4}
                    on_press: root.show_next()
                Button:
                    text: "X"
                    font_size: 16
                    size_hint: .05, .07
                    pos_hint: {'center_x': .975, 'center_y': .96}
                    on_press: popup.dismiss()
"""
