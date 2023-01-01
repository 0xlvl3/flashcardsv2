# Modules.
from files.create_deck import create_deck
from files.add_flashcard import add_flashcard
from files.play_cards import play_cards
from files.inspect_deck import inspect_deck
from files.delete_deck import delete_deck
from files.open_menu import open_menu

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


main()
