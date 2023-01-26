from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    """
    HomeScreen will be used to navigate the user.
    """

    def navigate_to_screen(self, screen_name):
        """
        Function will take user to specified screen
        """
        self.manager.current = screen_name

    def create_deck_screen(self):
        """
        Function will take user to create deck screen.
        """
        self.navigate_to_screen("create_deck_screen")

    def go_to_add_flashcard(self):
        """
        Function will take user to add flashcard screen.
        """
        self.navigate_to_screen("add_flashcard_screen")

    def go_to_inspect_deck(self):
        """
        Function will take user to inspect deck screen.
        """
        self.navigate_to_screen("inspect_deck_screen")

    def go_to_delete(self):
        """
        Function will take user to delete deck screen.
        """
        self.navigate_to_screen("delete_deck_screen")

    def go_to_play(self):
        """
        Function will take user to play deck screen.
        """
        self.navigate_to_screen("play_deck_screen")


kv_homescreen = """
<HomeScreen>:
    FloatLayout:
        Label:
            text: 'Welcome User'
            font_size: 28
            pos_hint: {'center_x':.5, 'center_y':.85}
        Label:
            text: 'Select an option below'
            font_size: 16
            pos_hint: {'center_x': .5, 'center_y': .8}
        Button:
            text: "Create Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .7}
            size_hint: .35, .07
			on_press: root.create_deck_screen() 
        Button:
            text: "Add Flashcards"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint: .35, .07
			on_press: root.go_to_add_flashcard()
        Button:
            text: "Inspect Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .35, .07
			on_press: root.go_to_inspect_deck()
        Button:
            text: "Play Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint: .35, .07
			on_press: root.go_to_play()
        Button:
            text: "Delete Deck"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .35, .07
			on_press: root.go_to_delete()
        Button:
            text: "Exit Application"
            font_size: 20
            pos_hint: {'center_x': .5, 'center_y': .1}
            size_hint: .35, .07
			on_press: app.stop()
"""
