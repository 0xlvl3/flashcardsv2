import os
import json


def write_file(deck_choice):
    with open(f"{deck_choice}/flashcard.json", "w") as cards:
        flashcards = {}
        json.dump(flashcards, cards)
        print(f"\n{deck_choice} has been created, go add flashcards!")


def check_if_flashcard_exists(question, answer, json_data):
    """
    Function checks if flashcard is already apart of user specified deck.
    """

    if question in json_data and json_data[question] == answer:
        return True
    return False


def user_choice_deck(deck, question, answer):
    """
    Function takes user choice to create a new deck
    while in add_flashcard function; this function will
    create the deck and also put flashcard in that deck.
    """

    user_choice = input(
        f"\n{deck} doesn't exist do you want to create it? Y/N:  "
    ).lower()

    if user_choice.lower() == "y":
        os.mkdir(deck)
        print(f"\n{deck} has been created! flashcard {question} has been added too!")
        with open(f"{deck}/flashcard.json", "w") as cards:
            flashcards = {question: answer}
            json.dump(flashcards, cards, indent=4)

    else:
        print("Returning to menu")
