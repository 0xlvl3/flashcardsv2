from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.app import App
from deck_module import user_deck


class InspectDeckScreen(Screen):
    def update_text(self, widget_id, message):
        self.manager.current_screen.ids[widget_id].text = message

    def get_text(self, widget_id):
        return self.manager.current_screen.ids[widget_id].text

    def index_cards(self):
        """
        Function will load user specified deck, deck will be saved to
        an index that will be iterated over.
        """
        user_choice = self.get_text("deck_to_inspect")
        token = App.get_running_app().logged_token
        # self.manager.current_screen.ids.load_deck.text = f"{user_choice} deck loaded"
        if user_choice == "":
            self.update_text(
                "error", "Text field is empty, please enter a deck and try again."
            )
        else:
            try:
                self.flashcards_indexed = user_deck.inspect_deck(token, user_choice)
                self.ins_index = 0

                self.ids.popup.open()
            except Exception as e:
                self.update_text("deck_to_inspect", "")
                e = f"Deck doesn't exist: {user_choice}"
                self.update_text("error", e)

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
            self.update_text(
                "question", "All flashcards have been shown. Resetting please wait."
            )
            Clock.schedule_once(self.reset_flashcards, 2)

    def reset_flashcards(self, time):
        """
        Function is used at the end of card loop, placed in Clock callback.
        """
        self.manager.current_screen.ids.deck_to_inspect.text = ""
        self.update_text("error", "")
        self.ids.popup.dismiss()

    def return_home(self):
        """
        Function will return the user back to the home screen.
        """
        self.update_text("error", "")
        self.manager.current = "home_screen"


kv_inspectdeckscreen = """
<InspectDeckScreen>:
    FloatLayout:
        id: ins_screen
        MDLabel:
            text: 'Deck Inspector'
            font_size: 48
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': .8}
        MDLabel:
            text: ''
            id: error
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .6}
            halign: 'center'
        MDTextField:
            mode: 'rectangle'
            multiline: False
            write_tab: False
            front_size: 18
            id: deck_to_inspect
            hint_text: 'Deck name'
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .4, .11
        MDFillRoundFlatButton:
            text: "Load deck"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .35, .1
            on_press: root.index_cards()
        MDFillRoundFlatButton:
            text: "Home"
            pos_hint:{'center_x': .5, 'center_y': .15}
            font_size: 24
            size_hint: .35, .1
            on_press: root.return_home()
        Popup:
            id: popup
            on_parent: if self.parent == ins_screen: ins_screen.remove_widget(self)
            title: 'Deck Inspector'
            content: popupcontent
            size_hint: .7, .7
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
