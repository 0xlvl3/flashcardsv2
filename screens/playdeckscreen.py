from kivy.uix.screenmanager import Screen
from deck_module import user_deck
from helper import get_text
from helper import update_text
from helper import go_to_screen
from helper import get_token
from constants import HOME_SCREEN

# -- Todo
# Fix up how play works, refactor the buttons and how it works in popup.


class PlayDeckScreen(Screen):
    def play(self):
        """
        Function will load deck and place it within an indexed array.
        """
        user_choice = get_text(self, "deck_to_play")
        USER_TOKEN = get_token()

        if user_choice == "":
            update_text(
                self,
                "error",
                "Please choose a deck, field is empty.",
            )
            update_text(self, "deck_to_play", "")
        else:
            try:
                self.flashcards_indexed = user_deck.inspect_deck(
                    USER_TOKEN, user_choice
                )
                self.index = 0
                self.correct = 0
                self.incorrect = 0

                if self.index < len(self.flashcards_indexed):
                    (
                        self.card_index,
                        self.question,
                        self.answer,
                    ) = self.flashcards_indexed[self.index]
                    update_text(
                        self,
                        "question_message",
                        f"{user_choice} loaded. Click next to start!",
                    )
                    update_text(self, "error", "")

                    self.ids.popup.open()
                else:
                    update_text(
                        self,
                        "question_message",
                        "All flashcards have been shown.",
                    )
                    update_text(
                        self,
                        "after_answer",
                        "Click the x to the right to exit.",
                    )
            except Exception as e:
                update_text(self, "deck_to_play", "")
                e = f"Deck doesn't exist: {user_choice}"
                update_text(self, "error", e)

    def check_answer(self):
        """
        Function will check to see if answer is equal to the user input.
        """
        user_answer = get_text(self, "answer")
        if user_answer == self.answer:
            update_text(self, "after_answer", f"Correct! answer was {self.answer}")
            update_text(self, "answer", "")
            self.correct += 1
        else:
            update_text(
                self, "after_answer", f"Incorrect the answer was: {self.answer}"
            )
            update_text(self, "answer", "")
            self.incorrect += 1

    def next_card(self):
        """
        Function will go to the next card in the indexed array.
        """
        if self.index < len(self.flashcards_indexed):
            self.card_index, self.question, self.answer = self.flashcards_indexed[
                self.index
            ]
            update_text(
                self,
                "question_message",
                f"{self.card_index}. Question: {self.question}",
            )
            update_text(self, "after_answer", "What is the answer?")
            self.index += 1
        else:
            update_text(
                self,
                "question_message",
                f"""
             All flashcards have been shown.
             You got {self.correct} correct and {self.incorrect} incorrect.
        To go back to the deck load screen, hit the x.
""",
            )
            update_text(self, "after_answer", "")
            update_text(self, "deck_to_play", "")

    def return_home(self):
        """
        Function will take user to the home screen.
        """
        go_to_screen(self, HOME_SCREEN)


kv_playdeckscreen = """
<PlayDeckScreen>:
    FloatLayout:
        id: play_screen
        MDLabel:
            text: 'Deck Player'
            font_size: 48
            pos_hint: {'center_x': .5, 'center_y': .75}
            halign: 'center'
        MDLabel:
            text: ''
            id: error
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .6}
            halign: 'center'
        MDTextField:
            mode: 'rectangle'
            font_size: 18
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .4, .11
            hint_text: "Deck to Play"
            id: deck_to_play
            write_tab: False
            multiline: False
        MDFillRoundFlatButton:
            text: "Load deck"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .4, .1
            on_press: root.play()
        MDFillRoundFlatButton:
            text: "Home"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .15}
            size_hint: .4, .1
            on_press: root.return_home()
        Popup:
            id: popup
            on_parent: if self.parent == play_screen: play_screen.remove_widget(self)
            title: 'Deck Player'
            content: popupcontent
            size_hint: .8, .8
            pos_hint: {'center_x': .5, 'center_y': .5}
            auto_dismiss: False
            FloatLayout:
                id:popupcontent
                Label:
                    text: 'Deck loaded'
                    id: after_answer
                    pos_hint: {'center_x': .5, 'center_y': .9}
                    size_hint: .2, .2
                Label:
                    text: 'Deck'
                    id: question_message
                    font_size: 24
                    pos_hint: {'center_x': .5, 'center_y': .8}
                    size_hint: .2, .2
                TextInput:
                    id: answer
                    write_tab: False
                    multiline: False
                    hint_text: 'Answer here'
                    font_size: 16
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    size_hint: .7, .1
                Button:
                    text: "Next"
                    font_size: 20
                    size_hint: .3, .15
                    pos_hint: {'center_x': .75, 'center_y': .2}
                    on_press: root.next_card()
                Button:
                    text: "Check Answer"
                    font_size: 20
                    size_hint: .3, .15
                    pos_hint: {'center_x': .25, 'center_y': .2}
                    on_press: root.check_answer()
                Button:
                    text: "X"
                    font_size: 20
                    size_hint: .05, .07
                    pos_hint: {'center_x': .975, 'center_y': .96}
                    on_press: popup.dismiss()
"""
