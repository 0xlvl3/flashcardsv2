# Kivy imports.
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Module imports.
from deck_module import user_deck

# Helper functions.
from helper import (
    get_text,
    update_text,
    go_to_screen,
    get_token, 
    show_button
)

# Constants.
from constants import HOME_SCREEN


class PlayDeckScreen(MDScreen):
    def play(self):
        """
        Function will load deck and place it within an indexed array.
        """
        user_choice = get_text(self, "deck_to_play")
        USER_TOKEN = get_token()

        # Check to see if user has text in field.

        if not user_choice:
            update_text(
                self,
                "error",
                "Please choose a deck, field is empty.",
            )
            update_text(self, "deck_to_play", "")
        else:

            # Index the deck that user entered and start play popup.

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
                    self.ids.next_btn.opacity = 1
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
            except Exception as e:  # It is very risky to catch all exceptions (see extended description)
                update_text(self, "deck_to_play", "")
                e = f"Deck doesn't exist: {user_choice}"
                update_text(self, "error", e)

    def check_answer(self):
        """
        Function will check to see if answer is equal to the user input.
        Will give back a string if correct or incorrect and show next_btn and hide check_btn.
        """
        user_answer = get_text(self, "answer")
        if user_answer == self.answer:
            update_text(self, "after_answer", f"Correct! answer was {self.answer}")
            update_text(self, "answer", "")
            self.correct += 1
            show_button(self, "check_btn", "next_btn")

        else:
            update_text(
                self, "after_answer", f"Incorrect the answer was: {self.answer}"
            )
            update_text(self, "answer", "")
            self.incorrect += 1
            show_button(self, "check_btn", "next_btn")

    def next_card(self):
        """
        Function will go to the next card in the indexed array after check_answer complete.
        Will hide check_btn and show next_btn
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
            show_button(self, "next_btn", "check_btn")

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
            self.ids.next_btn.opacity = 0

    def return_home(self):
        """
        Function will take user to the home screen.
        """
        update_text(self, "error", "")
        go_to_screen(self, HOME_SCREEN)


kv_playdeckscreen = """
<PlayDeckScreen>:
    MDFloatLayout:
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
        MDRaisedButton:
            text: "Load deck"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .4, .1
            on_press: root.play()
        MDRaisedButton:
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
            MDFloatLayout:
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
                    pos_hint: {'center_x': .5, 'center_y': .75}
                    size_hint: .2, .2
                MDTextField:
                    id: answer
                    write_tab: False
                    multiline: False
                    mode: 'rectangle'
                    text_color_normal: 'white'
                    text_color_focus: 'white'
                    set_text_color_normal: 'white'
                    line_color_focus: "white"
                    line_color_normal: 'white'
                    helper_text_color_normal: 'white'
                    helper_text_color_focus: 'white'
                    helper_text: 'Answer here'
                    helper_text_mode: 'persistent'
                    font_size: 18
                    pos_hint: {'center_x': .5, 'center_y': .5}
                MDRaisedButton:
                    id: next_btn
                    text: "Next"
                    font_size: 20
                    size_hint: .35, .1
                    pos_hint: {'center_x': .75, 'center_y': .2}
                    opacity: 1
                    on_press: root.next_card()
                MDRaisedButton:
                    id: check_btn
                    text: "Check Answer"
                    font_size: 20
                    size_hint: .35, .1
                    pos_hint: {'center_x': .25, 'center_y': .2}
                    opacity: 0
                    on_press: root.check_answer()
                MDRaisedButton:
                    text: "X"
                    font_size: 18
                    size_hint: .02, .02
                    pos_hint: {'center_x': .95, 'center_y': .95}
                    on_press: popup.dismiss()
"""

Builder.load_string(kv_playdeckscreen)
