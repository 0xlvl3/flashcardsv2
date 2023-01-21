from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    def switch_cards_screen(self):
        self.manager.current = "cards_screen"

    def create_deck_screen(self):
        self.manager.current = "create_deck_screen"

    def go_to_add_flashcard(self):
        self.manager.current = "add_flashcard_screen"

    def go_to_inspect_deck(self):
        self.manager.current = "inspect_deck_screen"

    def go_to_delete(self):
        self.manager.current = "delete_deck_screen"

    def go_to_play(self):
        self.manager.current = "play_deck_screen"
