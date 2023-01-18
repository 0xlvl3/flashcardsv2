import os
import json


def play_cards():
    """
    Function will play through flashcards; user will be
    asked a question and prompted for an answer until deck
    has no cards left.
    """
    deck_choice = input("Which deck do you want to run through? ").lower()

    # If directory exists game starts.
    if os.path.exists(deck_choice):
        with open(f"{deck_choice}/flashcard.json", "r") as f:
            data = json.load(f)

            # Game counters.
            card_count = 0
            correct = 0
            incorrect = 0

            # Card loop.
            for question, answer in data.items():
                card_count += 1
                print(f"\n{card_count}. {question}")
                user_answer = input("Type answer here: ").lower()
                if user_answer == answer:
                    correct += 1
                else:
                    incorrect += 1

        # Play score.
        print(
            f"""
(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧・ﾟ✧
Out of {card_count} you got {correct} correct and {incorrect} incorrect
                        """
        )

    # If directory doesn't exist return to menu.
    else:
        print(f"\n### {deck_choice} deck does not exist returning to menu")
