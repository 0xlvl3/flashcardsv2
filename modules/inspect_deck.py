import os
import json
from modules.utilities_funcs import write_file


def inspect_deck():
    """
    Function will return a list of cards within a specified deck.
    """
    deck_choice = input("Name of the deck you wish to inspect: ").lower()

    # If deck exists.
    if os.path.exists(deck_choice):
        json_file = None
        for flashcards in os.listdir(deck_choice):
            if flashcards.endswith(".json"):
                json_file = flashcards
            print(f"\nThese are the current flashcards in {deck_choice}")
            with open(os.path.join(deck_choice, json_file)) as card_list:
                data = json.load(card_list)
                counter = 1
                for question, answer in data.items():
                    print(
                        f"""
            +---------------------------------------
          {counter}.| Question: {question}
            | Answer: {answer}
                        """
                    )
                    counter += 1

            print("\nDeck list finished! go add more")
    # If deck doesn't exist.
    else:
        user_answer = input(
            f"\n{deck_choice} doesn't exist do you want to create it? Y/N:  "
        ).lower()
        if user_answer.lower() == "y":
            os.mkdir(deck_choice)
            write_file(deck_choice)
        else:
            print("\n### Returning to menu")
