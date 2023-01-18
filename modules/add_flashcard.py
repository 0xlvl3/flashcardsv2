import os
import json
from modules.utilities_funcs import check_if_flashcard_exists
from modules.utilities_funcs import user_choice_deck


def add_flashcard():
    """
    Function will add a 'question' + 'answer' into a json
    within a specified directory; won't add dupe flashcards.
    """
    # Ask the user for the flashcard question and answer.
    question = input("\nEnter the flashcard question: ").lower()
    answer = input("Enter the flashcard answer: ").lower()

    user_named_deck = input("Name of the deck you wish to add this card: ").lower()

    # Check if directory exists.
    if os.path.isdir(user_named_deck):
        with open(f"{user_named_deck}/flashcard.json", "r") as cards:
            flashcards = json.load(cards)

            # Checks if card is a duplicate.
            if check_if_flashcard_exists(question, answer, flashcards):
                print(
                    f"""
\n### The "{question}" flashcard in {user_named_deck} already exists!
Returning to menu                     
                    """
                )

            # Add the flashcard to the dictionary.
            else:
                flashcards[question] = answer
                print(f'\n### "{question}" card has been added to {user_named_deck}')
                with open(f"{user_named_deck}/flashcard.json", "w") as cards:
                    json.dump(flashcards, cards, indent=4)

    # If directory doesn't exists; Will create and add card to that directory.
    else:
        user_choice_deck(user_named_deck, question, answer)
