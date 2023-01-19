# Kivy / GUI.
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


# Modules.
from modules.create_deck import create_deck
from modules.add_flashcard import add_flashcard
from modules.play_cards import play_cards
from modules.inspect_deck import inspect_deck
from modules.delete_deck import delete_deck
from modules.open_menu import open_menu
from firebase import signup
from firebase import user_login

Builder.load_file("frontend.kv")


class StartScreen(Screen):
    def create_account(self):
        self.manager.current = "create_screen"

    def go_to_login(self):
        self.manager.current = "login_screen"


class CreateScreen(Screen):
    def create(self):
        email = self.manager.current_screen.ids.user_email.text
        password = self.manager.current_screen.ids.user_password.text
        signup(email, password)
        print("Account created")
        self.manager.current = "login_screen"


class LoginScreen(Screen):
    def login(self):
        print("Logging in")
        email = self.manager.current_screen.ids.login_email.text
        password = self.manager.current_screen.ids.login_password.text
        user_login(email, password)
        self.manager.current = "home_screen"


class HomeScreen(Screen):
    def switch_cards_screen(self):
        self.manager.current = "cards_screen"


class CardsScreen(Screen):
    def back_to_start(self):
        self.manager.current = "start_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


flashcards = {}


open_menu("menu.txt")


def main():
    """
    Main loop for our flashcards program
    """

    while True:
        print("\n'ls' to see the menu again")
        action = input("choose an action: ").lower()

        if action == "c":
            create_deck()
        elif action == "a":
            add_flashcard()
        elif action == "p":
            play_cards()
        elif action == "i":
            inspect_deck()
        elif action == "d":
            delete_deck()
        elif action == "ls":
            open_menu("menu.txt")
        elif action == "e":
            exit()


# main()

MainApp().run()
