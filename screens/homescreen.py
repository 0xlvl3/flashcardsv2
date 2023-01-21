from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    """
    HomeScreen will be used to navigate the user.
    """

    def switch_cards_screen(self):
        """
        Function will take user to cards screen.
        """
        self.manager.current = "cards_screen"

    def create_deck_screen(self):
        """
        Function will take user to create deck screen.
        """
        self.manager.current = "create_deck_screen"

    def go_to_add_flashcard(self):
        """
        Function will take user to add flashcard screen.
        """
        self.manager.current = "add_flashcard_screen"

    def go_to_inspect_deck(self):
        """
        Function will take user to inspect deck screen.
        """
        self.manager.current = "inspect_deck_screen"

    def go_to_delete(self):
        """
        Function will take user to delete deck screen.
        """
        self.manager.current = "delete_deck_screen"

    def go_to_play(self):
        """
        Function will take user to play deck screen.
        """
        self.manager.current = "play_deck_screen"
