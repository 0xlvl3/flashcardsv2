import os
import json


def create_deck():
    """
    Function creates a directory or 'Deck' that will
    house our flashcards.json.
    """

    print("\n### Deck will be saved all lowercase")
    userInput = input(f"\nName your new deck: ").lower()

    # Check to see if directory exists.
    if not os.path.exists(userInput):
        os.mkdir(userInput)
        with open(f"{userInput}/flashcard.json", "w") as cards:
            flashcards = {}
            json.dump(flashcards, cards)
            print(f"\n{userInput} has been created, go add flashcards!")

    else:
        print(f"\n### {userInput} already exists! returning you to menu")
